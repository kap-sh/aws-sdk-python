"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateGatewayBridgeSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.vpc_interface_attachment


class UpdateGatewayBridgeSourceRequest(TypedDict):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge feeding this flow.</p>"""
    vpc_interface_attachment: NotRequired[
        "aws_sdk_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"
    ]
    """<p> The name of the VPC interface attachment to use for this bridge source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayBridgeSourceRequest) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "vpc_interface_attachment" in value:
        import aws_sdk_mediaconnect.types.vpc_interface_attachment

        out["vpcInterfaceAttachment"] = (
            aws_sdk_mediaconnect.types.vpc_interface_attachment.serialize_json(
                value["vpc_interface_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGatewayBridgeSourceRequest:
    out: UpdateGatewayBridgeSourceRequest = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "vpcInterfaceAttachment" in data:
        import aws_sdk_mediaconnect.types.vpc_interface_attachment

        out["vpc_interface_attachment"] = (
            aws_sdk_mediaconnect.types.vpc_interface_attachment.deserialize_json(
                data["vpcInterfaceAttachment"]
            )
        )
    return out
