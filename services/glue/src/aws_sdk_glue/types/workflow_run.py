"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowRun``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_string
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.starting_event_batch_condition
    import aws_sdk_glue.types.timestamp_value
    import aws_sdk_glue.types.workflow_graph
    import aws_sdk_glue.types.workflow_run_properties
    import aws_sdk_glue.types.workflow_run_statistics
    import aws_sdk_glue.types.workflow_run_status


class WorkflowRun(TypedDict):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Name of the workflow that was run.</p>"""
    workflow_run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The ID of this workflow run.</p>"""
    previous_run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The ID of the previous workflow run.</p>"""
    workflow_run_properties: NotRequired[
        "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties"
    ]
    """<p>The workflow run properties which were set during the run.</p>"""
    started_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time when the workflow run was started.</p>"""
    completed_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time when the workflow run completed.</p>"""
    status: NotRequired["aws_sdk_glue.types.workflow_run_status.WorkflowRunStatus"]
    """<p>The status of the workflow run.</p>"""
    error_message: NotRequired["aws_sdk_glue.types.error_string.ErrorString"]
    r"""<p>This error message describes any error that may have occurred in starting the workflow run. Currently the only error message is \"Concurrent runs exceeded for workflow: <code>foo</code>.\"</p>"""
    statistics: NotRequired[
        "aws_sdk_glue.types.workflow_run_statistics.WorkflowRunStatistics"
    ]
    """<p>The statistics of the run.</p>"""
    graph: NotRequired["aws_sdk_glue.types.workflow_graph.WorkflowGraph"]
    """<p>The graph representing all the Glue components that belong to the workflow as nodes and directed connections between them as edges.</p>"""
    starting_event_batch_condition: NotRequired[
        "aws_sdk_glue.types.starting_event_batch_condition.StartingEventBatchCondition"
    ]
    """<p>The batch condition that started the workflow run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowRun) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "workflow_run_id" in value:
        out["WorkflowRunId"] = value["workflow_run_id"]
    if "previous_run_id" in value:
        out["PreviousRunId"] = value["previous_run_id"]
    if "workflow_run_properties" in value:
        import aws_sdk_glue.types.workflow_run_properties

        out["WorkflowRunProperties"] = (
            aws_sdk_glue.types.workflow_run_properties.serialize_aws_json_1_1(
                value["workflow_run_properties"]
            )
        )
    if "started_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["StartedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "completed_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CompletedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "status" in value:
        import aws_sdk_glue.types.workflow_run_status

        out["Status"] = aws_sdk_glue.types.workflow_run_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "statistics" in value:
        import aws_sdk_glue.types.workflow_run_statistics

        out["Statistics"] = (
            aws_sdk_glue.types.workflow_run_statistics.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    if "graph" in value:
        import aws_sdk_glue.types.workflow_graph

        out["Graph"] = aws_sdk_glue.types.workflow_graph.serialize_aws_json_1_1(
            value["graph"]
        )
    if "starting_event_batch_condition" in value:
        import aws_sdk_glue.types.starting_event_batch_condition

        out["StartingEventBatchCondition"] = (
            aws_sdk_glue.types.starting_event_batch_condition.serialize_aws_json_1_1(
                value["starting_event_batch_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowRun:
    out: WorkflowRun = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "WorkflowRunId" in data:
        out["workflow_run_id"] = data["WorkflowRunId"]
    if "PreviousRunId" in data:
        out["previous_run_id"] = data["PreviousRunId"]
    if "WorkflowRunProperties" in data:
        import aws_sdk_glue.types.workflow_run_properties

        out["workflow_run_properties"] = (
            aws_sdk_glue.types.workflow_run_properties.deserialize_aws_json_1_1(
                data["WorkflowRunProperties"]
            )
        )
    if "StartedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["started_on"] = aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "CompletedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["completed_on"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["CompletedOn"]
            )
        )
    if "Status" in data:
        import aws_sdk_glue.types.workflow_run_status

        out["status"] = aws_sdk_glue.types.workflow_run_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "Statistics" in data:
        import aws_sdk_glue.types.workflow_run_statistics

        out["statistics"] = (
            aws_sdk_glue.types.workflow_run_statistics.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    if "Graph" in data:
        import aws_sdk_glue.types.workflow_graph

        out["graph"] = aws_sdk_glue.types.workflow_graph.deserialize_aws_json_1_1(
            data["Graph"]
        )
    if "StartingEventBatchCondition" in data:
        import aws_sdk_glue.types.starting_event_batch_condition

        out["starting_event_batch_condition"] = (
            aws_sdk_glue.types.starting_event_batch_condition.deserialize_aws_json_1_1(
                data["StartingEventBatchCondition"]
            )
        )
    return out
