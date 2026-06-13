"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateGatewayInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_placement


class UpdateGatewayInstanceResponse(TypedDict):
    bridge_placement: NotRequired[
        "aws_sdk_mediaconnect.types.bridge_placement.BridgePlacement"
    ]
    """<p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>"""
    gateway_instance_arn: NotRequired["str"]
    """<p>The ARN of the instance that was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayInstanceResponse) -> dict:
    out: dict = {}
    if "bridge_placement" in value:
        import aws_sdk_mediaconnect.types.bridge_placement

        out["bridgePlacement"] = (
            aws_sdk_mediaconnect.types.bridge_placement.serialize_json(
                value["bridge_placement"]
            )
        )
    if "gateway_instance_arn" in value:
        out["gatewayInstanceArn"] = value["gateway_instance_arn"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayInstanceResponse:
    out: UpdateGatewayInstanceResponse = {}  # type: ignore[typeddict-item]
    if "bridgePlacement" in data:
        import aws_sdk_mediaconnect.types.bridge_placement

        out["bridge_placement"] = (
            aws_sdk_mediaconnect.types.bridge_placement.deserialize_json(
                data["bridgePlacement"]
            )
        )
    if "gatewayInstanceArn" in data:
        out["gateway_instance_arn"] = data["gatewayInstanceArn"]
    return out
