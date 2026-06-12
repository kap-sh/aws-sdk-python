"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgeFlowSource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.vpc_interface_attachment

class BridgeFlowSource(TypedDict):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the cloud flow used as a source of this bridge.</p>"""
    flow_vpc_interface_attachment: NotRequired["aws_sdk_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"]
    """<p> The name of the VPC interface attachment to use for this source.</p>"""
    name: NotRequired["str"]
    """<p> The name of the flow source.</p>"""
    output_arn: NotRequired["str"]
    """<p> The Amazon Resource Number (ARN) of the output.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BridgeFlowSource) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_vpc_interface_attachment" in value:
        import aws_sdk_mediaconnect.types.vpc_interface_attachment
        out["flowVpcInterfaceAttachment"] = aws_sdk_mediaconnect.types.vpc_interface_attachment.serialize_json(value["flow_vpc_interface_attachment"])
    if "name" in value:
        out["name"] = value["name"]
    if "output_arn" in value:
        out["outputArn"] = value["output_arn"]
    return out


def deserialize_json(data: dict) -> BridgeFlowSource:
    out: BridgeFlowSource = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowVpcInterfaceAttachment" in data:
        import aws_sdk_mediaconnect.types.vpc_interface_attachment
        out["flow_vpc_interface_attachment"] = aws_sdk_mediaconnect.types.vpc_interface_attachment.deserialize_json(data["flowVpcInterfaceAttachment"])
    if "name" in data:
        out["name"] = data["name"]
    if "outputArn" in data:
        out["output_arn"] = data["outputArn"]
    return out