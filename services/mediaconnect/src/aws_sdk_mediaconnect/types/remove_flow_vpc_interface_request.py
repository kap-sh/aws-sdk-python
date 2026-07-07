"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowVpcInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn


class RemoveFlowVpcInterfaceRequest(TypedDict, closed=True):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to remove a VPC interface from.</p>"""
    vpc_interface_name: "str"
    """<p> The name of the VPC interface that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowVpcInterfaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveFlowVpcInterfaceRequest:
    out: RemoveFlowVpcInterfaceRequest = {}  # type: ignore[typeddict-item]
    return out
