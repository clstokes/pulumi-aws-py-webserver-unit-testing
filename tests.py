import pulumi
import unittest
import asyncio

# Import the Pulumi SDK and turn on test mode *before* allocating anything.
pulumi.runtime.settings._set_test_mode_enabled(True)                         # ref: https://github.com/pulumi/pulumi/issues/2818
pulumi.runtime.settings._set_project('pulumi-aws-py-webserver-unit-testing')
pulumi.runtime.settings._set_stack('fake-stack')


# Tests come next:
def async_test(coro):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(coro(*args, **kwargs))
        loop.close()
    return wrapper


class InstanceTests(unittest.TestCase):

    @async_test
    async def test_no_internet_access(self):
        from infra import group

        # Rendezvous with the resource's resulting attributes
        resource_fut = asyncio.Future()
        group.ingress.apply(lambda res: resource_fut.set_result(res))
        ingress = await resource_fut

        # Loop through ingress rules and reject any that are open to the Internet (0.0.0.0/0).
        for rule in ingress:
            for cidr in rule['cidr_blocks']:
                self.assertNotEqual('0.0.0.0/0', cidr)

    @async_test
    async def test_no_userdata(self):
        from infra import server

        # Rendezvous with the resource's resulting attributes
        resource_fut = asyncio.Future()
        server.user_data.apply(lambda res: resource_fut.set_result(res))
        user_data = await resource_fut

        # Check user_data
        self.assertIsNone(user_data)
