"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateGatewayInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_placement


class UpdateGatewayInstanceResponse(TypedDict, closed=True):
    bridge_placement: NotRequired[
        "capo_mediaconnect.types.bridge_placement.BridgePlacement"
    ]
    """<p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>"""
    gateway_instance_arn: NotRequired["str"]
    """<p>The ARN of the instance that was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayInstanceResponse) -> dict:
    out: dict = {}
    if "bridge_placement" in value:
        import capo_mediaconnect.types.bridge_placement

        out["bridgePlacement"] = (
            capo_mediaconnect.types.bridge_placement.serialize_json(
                value["bridge_placement"]
            )
        )
    if "gateway_instance_arn" in value:
        out["gatewayInstanceArn"] = value["gateway_instance_arn"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayInstanceResponse:
    out: UpdateGatewayInstanceResponse = {}  # type: ignore[typeddict-item]
    if "bridgePlacement" in data:
        import capo_mediaconnect.types.bridge_placement

        out["bridge_placement"] = (
            capo_mediaconnect.types.bridge_placement.deserialize_json(
                data["bridgePlacement"]
            )
        )
    if "gatewayInstanceArn" in data:
        out["gateway_instance_arn"] = data["gatewayInstanceArn"]
    return out
