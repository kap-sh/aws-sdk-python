"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateGatewayInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_placement
    import aws_sdk_mediaconnect.types.gateway_instance_arn


class UpdateGatewayInstanceRequest(TypedDict, closed=True):
    bridge_placement: NotRequired[
        "aws_sdk_mediaconnect.types.bridge_placement.BridgePlacement"
    ]
    """<p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>"""
    gateway_instance_arn: (
        "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the gateway instance that you want to update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayInstanceRequest) -> dict:
    out: dict = {}
    if "bridge_placement" in value:
        import aws_sdk_mediaconnect.types.bridge_placement

        out["bridgePlacement"] = (
            aws_sdk_mediaconnect.types.bridge_placement.serialize_json(
                value["bridge_placement"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGatewayInstanceRequest:
    out: UpdateGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
    if "bridgePlacement" in data:
        import aws_sdk_mediaconnect.types.bridge_placement

        out["bridge_placement"] = (
            aws_sdk_mediaconnect.types.bridge_placement.deserialize_json(
                data["bridgePlacement"]
            )
        )
    return out
