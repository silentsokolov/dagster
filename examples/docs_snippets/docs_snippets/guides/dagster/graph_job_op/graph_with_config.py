from dagster import job, op


@op(config_schema={"param": str})
def do_something(_):
    ...


default_config = {"ops": {"do_something": {"config": {"param": "some_val"}}}}


@job(config=default_config)
def do_it_all():
    do_something()
