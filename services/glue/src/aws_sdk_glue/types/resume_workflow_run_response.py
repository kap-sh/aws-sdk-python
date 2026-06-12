"""Generated from Smithy shape ``com.amazonaws.glue#ResumeWorkflowRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.node_id_list


class ResumeWorkflowRunResponse(TypedDict):
    run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The new ID assigned to the resumed workflow run. Each resume of a workflow run will have a new run ID.</p>"""
    node_ids: NotRequired["aws_sdk_glue.types.node_id_list.NodeIdList"]
    """<p>A list of the node IDs for the nodes that were actually restarted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResumeWorkflowRunResponse) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "node_ids" in value:
        import aws_sdk_glue.types.node_id_list

        out["NodeIds"] = aws_sdk_glue.types.node_id_list.serialize_aws_json_1_1(
            value["node_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResumeWorkflowRunResponse:
    out: ResumeWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "NodeIds" in data:
        import aws_sdk_glue.types.node_id_list

        out["node_ids"] = aws_sdk_glue.types.node_id_list.deserialize_aws_json_1_1(
            data["NodeIds"]
        )
    return out
