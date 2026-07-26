"""Generated from Smithy shape ``com.amazonaws.glue#Workflow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.blueprint_details
    import capo_glue.types.generic_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.timestamp_value
    import capo_glue.types.workflow_graph
    import capo_glue.types.workflow_run
    import capo_glue.types.workflow_run_properties


class Workflow(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the workflow.</p>"""
    description: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A description of the workflow.</p>"""
    default_run_properties: NotRequired[
        "capo_glue.types.workflow_run_properties.WorkflowRunProperties"
    ]
    """<p>A collection of properties to be used as part of each execution of the workflow. The run properties are made available to each job in the workflow. A job can modify the properties for the next jobs in the flow.</p>"""
    created_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time when the workflow was created.</p>"""
    last_modified_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time when the workflow was last modified.</p>"""
    last_run: NotRequired["capo_glue.types.workflow_run.WorkflowRun"]
    """<p>The information about the last execution of the workflow.</p>"""
    graph: NotRequired["capo_glue.types.workflow_graph.WorkflowGraph"]
    """<p>The graph representing all the Glue components that belong to the workflow as nodes and directed connections between them as edges.</p>"""
    max_concurrent_runs: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.</p>"""
    blueprint_details: NotRequired["capo_glue.types.blueprint_details.BlueprintDetails"]
    """<p>This structure indicates the details of the blueprint that this particular workflow is created from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workflow) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_run_properties" in value:
        import capo_glue.types.workflow_run_properties

        out["DefaultRunProperties"] = (
            capo_glue.types.workflow_run_properties.serialize_aws_json_1_1(
                value["default_run_properties"]
            )
        )
    if "created_on" in value:
        import capo_glue.types.timestamp_value

        out["CreatedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "last_modified_on" in value:
        import capo_glue.types.timestamp_value

        out["LastModifiedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    if "last_run" in value:
        import capo_glue.types.workflow_run

        out["LastRun"] = capo_glue.types.workflow_run.serialize_aws_json_1_1(
            value["last_run"]
        )
    if "graph" in value:
        import capo_glue.types.workflow_graph

        out["Graph"] = capo_glue.types.workflow_graph.serialize_aws_json_1_1(
            value["graph"]
        )
    if "max_concurrent_runs" in value:
        out["MaxConcurrentRuns"] = value["max_concurrent_runs"]
    if "blueprint_details" in value:
        import capo_glue.types.blueprint_details

        out["BlueprintDetails"] = (
            capo_glue.types.blueprint_details.serialize_aws_json_1_1(
                value["blueprint_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Workflow:
    out: Workflow = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultRunProperties" in data:
        import capo_glue.types.workflow_run_properties

        out["default_run_properties"] = (
            capo_glue.types.workflow_run_properties.deserialize_aws_json_1_1(
                data["DefaultRunProperties"]
            )
        )
    if "CreatedOn" in data:
        import capo_glue.types.timestamp_value

        out["created_on"] = capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if "LastModifiedOn" in data:
        import capo_glue.types.timestamp_value

        out["last_modified_on"] = (
            capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["LastModifiedOn"]
            )
        )
    if "LastRun" in data:
        import capo_glue.types.workflow_run

        out["last_run"] = capo_glue.types.workflow_run.deserialize_aws_json_1_1(
            data["LastRun"]
        )
    if "Graph" in data:
        import capo_glue.types.workflow_graph

        out["graph"] = capo_glue.types.workflow_graph.deserialize_aws_json_1_1(
            data["Graph"]
        )
    if "MaxConcurrentRuns" in data:
        out["max_concurrent_runs"] = data["MaxConcurrentRuns"]
    if "BlueprintDetails" in data:
        import capo_glue.types.blueprint_details

        out["blueprint_details"] = (
            capo_glue.types.blueprint_details.deserialize_aws_json_1_1(
                data["BlueprintDetails"]
            )
        )
    return out
