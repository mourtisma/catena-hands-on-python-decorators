
def call_frequency(max_freq: int) -> callable:
    # TODO: If our function is called more than max_freq times, raise an exception

@call_frequency(4)
def hello():
    print("Hello World")
