import inspect

# Decorator to capture function calls
def capture_calls(func):
    def wrapper(*args, **kwargs):
        # Get the function's name
        func_name = func.__name__
        # Capture arguments
        arguments = inspect.getcallargs(func, *args, **kwargs)
        print(f"Function call: {func_name}, Arguments: {arguments}")
        return func(*args, **kwargs)
    return wrapper

# Context manager to capture object creation
class CaptureObjects:
    def __init__(self):
        self.objects = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Objects created:")
        for obj in self.objects:
            print(obj)

    def track_object(self, obj):
        self.objects.append(obj)

# Decorator to capture object creation
def capture_objects(cls):
    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._capture_objects()

        def _capture_objects(self):
            with CaptureObjects() as capturer:
                capturer.track_object(self)
    return Wrapper
