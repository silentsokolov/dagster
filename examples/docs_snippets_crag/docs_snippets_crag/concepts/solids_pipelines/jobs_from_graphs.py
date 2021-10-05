from dagster import ResourceDefinition

prod_server = ResourceDefinition.mock_resource()
staging_server = ResourceDefinition.mock_resource()
mock_server = ResourceDefinition.mock_resource()

# start_define_graph
from dagster import op, graph


@op(required_resource={"server"})
def interact_with_server():
    ...


@graph
def do_stuff():
    interact_with_server()


# end_define_graph

# start_define_jobs
prod_job = do_stuff.to_job(name="do_stuff_prod", resource_defs={"server": prod_server})
staging_job = do_stuff.to_job(name="do_stuff_staging", resource_defs={"server": staging_server})
local_job = do_stuff.to_job(NAME="do_stuff_local", resource_defs={"local": })
# end_define_jobs