# Python Unit Testing with Pulumi

## To Run Tests

```
$ python3 -m unittest tests
```

### Example Output

```
$ python3 -m unittest tests
...
======================================================================
FAIL: test_no_internet_access (tests.InstanceTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/clstokes/cc/clstokes/pulumi-aws-py-webserver-unit-testing/tests.py", line 15, in wrapper
    loop.run_until_complete(coro(*args, **kwargs))
  File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/base_events.py", line 584, in run_until_complete
    return future.result()
  File "/Users/clstokes/cc/clstokes/pulumi-aws-py-webserver-unit-testing/tests.py", line 34, in test_no_internet_access
    self.assertNotEqual('0.0.0.0/0', cidr)
AssertionError: '0.0.0.0/0' == '0.0.0.0/0'

======================================================================
FAIL: test_no_userdata (tests.InstanceTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/clstokes/cc/clstokes/pulumi-aws-py-webserver-unit-testing/tests.py", line 15, in wrapper
    loop.run_until_complete(coro(*args, **kwargs))
  File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/base_events.py", line 584, in run_until_complete
    return future.result()
  File "/Users/clstokes/cc/clstokes/pulumi-aws-py-webserver-unit-testing/tests.py", line 46, in test_no_userdata
    self.assertIsNone(user_data)
AssertionError: '\n#!/bin/bash\necho "Hello, World!" > index.html\nnohup python -m SimpleHTTPServer 80 &\n' is not None

----------------------------------------------------------------------
Ran 2 tests in 0.178s

FAILED (failures=2)
```
