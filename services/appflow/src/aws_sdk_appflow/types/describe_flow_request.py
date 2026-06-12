"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.flow_name


class DescribeFlowRequest(TypedDict):
    flow_name: "aws_sdk_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    return out


def deserialize_json(data: dict) -> DescribeFlowRequest:
    out: DescribeFlowRequest = {}  # type: ignore[typeddict-item]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("DescribeFlowRequest.flow_name required")
    return out
