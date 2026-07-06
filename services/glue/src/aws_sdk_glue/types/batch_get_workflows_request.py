"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.workflow_names


class BatchGetWorkflowsRequest(TypedDict, closed=True):
    names: "aws_sdk_glue.types.workflow_names.WorkflowNames"
    """<p>A list of workflow names, which may be the names returned from the <code>ListWorkflows</code> operation.</p>"""
    include_graph: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to include a graph when returning the workflow resource metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetWorkflowsRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.workflow_names

    out["Names"] = aws_sdk_glue.types.workflow_names.serialize_aws_json_1_1(
        value["names"]
    )
    if "include_graph" in value:
        out["IncludeGraph"] = value["include_graph"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetWorkflowsRequest:
    out: BatchGetWorkflowsRequest = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import aws_sdk_glue.types.workflow_names

        out["names"] = aws_sdk_glue.types.workflow_names.deserialize_aws_json_1_1(
            data["Names"]
        )
    else:
        raise DeserializationError("BatchGetWorkflowsRequest.names required")
    if "IncludeGraph" in data:
        out["include_graph"] = data["IncludeGraph"]
    return out
