"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeFlowSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.vpc_interface_attachment


class UpdateBridgeFlowSourceRequest(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) that identifies the MediaConnect resource from which to delete tags.</p>"""
    flow_vpc_interface_attachment: NotRequired[
        "capo_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"
    ]
    """<p>The name of the VPC interface attachment to use for this source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeFlowSourceRequest) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_vpc_interface_attachment" in value:
        import capo_mediaconnect.types.vpc_interface_attachment

        out["flowVpcInterfaceAttachment"] = (
            capo_mediaconnect.types.vpc_interface_attachment.serialize_json(
                value["flow_vpc_interface_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeFlowSourceRequest:
    out: UpdateBridgeFlowSourceRequest = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowVpcInterfaceAttachment" in data:
        import capo_mediaconnect.types.vpc_interface_attachment

        out["flow_vpc_interface_attachment"] = (
            capo_mediaconnect.types.vpc_interface_attachment.deserialize_json(
                data["flowVpcInterfaceAttachment"]
            )
        )
    return out
