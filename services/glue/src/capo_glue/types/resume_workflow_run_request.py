"""Generated from Smithy shape ``com.amazonaws.glue#ResumeWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.id_string
    import capo_glue.types.name_string
    import capo_glue.types.node_id_list


class ResumeWorkflowRunRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the workflow to resume.</p>"""
    run_id: "capo_glue.types.id_string.IdString"
    """<p>The ID of the workflow run to resume.</p>"""
    node_ids: "capo_glue.types.node_id_list.NodeIdList"
    """<p>A list of the node IDs for the nodes you want to restart. The nodes that are to be restarted must have a run attempt in the original run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResumeWorkflowRunRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RunId"] = value["run_id"]
    import capo_glue.types.node_id_list

    out["NodeIds"] = capo_glue.types.node_id_list.serialize_aws_json_1_1(
        value["node_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResumeWorkflowRunRequest:
    out: ResumeWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ResumeWorkflowRunRequest.name required")
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("ResumeWorkflowRunRequest.run_id required")
    if "NodeIds" in data:
        import capo_glue.types.node_id_list

        out["node_ids"] = capo_glue.types.node_id_list.deserialize_aws_json_1_1(
            data["NodeIds"]
        )
    else:
        raise DeserializationError("ResumeWorkflowRunRequest.node_ids required")
    return out
