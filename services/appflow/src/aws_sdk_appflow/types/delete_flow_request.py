"""Generated from Smithy shape ``com.amazonaws.appflow#DeleteFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.flow_name


class DeleteFlowRequest(TypedDict, closed=True):
    flow_name: "aws_sdk_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    force_delete: "aws_sdk_appflow.types.boolean.Boolean"
    """<p> Indicates whether Amazon AppFlow should delete the flow, even if it is currently in use. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    out["forceDelete"] = value.get("force_delete", False)
    return out


def deserialize_json(data: dict) -> DeleteFlowRequest:
    out: DeleteFlowRequest = {}  # type: ignore[typeddict-item]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("DeleteFlowRequest.flow_name required")
    if "forceDelete" in data:
        out["force_delete"] = data["forceDelete"]
    else:
        out["force_delete"] = False
    return out
