from dagster import op, job


@op
def do_something():
    pass


@job
def do_stuff():
    do_something()
