"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedGateway``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.gateway_state


class ListedGateway(TypedDict):
    gateway_arn: NotRequired["str"]
    """<p> The Amazon Resource Name (ARN) of the gateway.</p>"""
    gateway_state: NotRequired["aws_sdk_mediaconnect.types.gateway_state.GatewayState"]
    """<p> The status of the gateway.</p>"""
    name: NotRequired["str"]
    """<p> The name of the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedGateway) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "gateway_state" in value:
        import aws_sdk_mediaconnect.types.gateway_state

        out["gatewayState"] = aws_sdk_mediaconnect.types.gateway_state.serialize_json(
            value["gateway_state"]
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ListedGateway:
    out: ListedGateway = {}  # type: ignore[typeddict-item]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    if "gatewayState" in data:
        import aws_sdk_mediaconnect.types.gateway_state

        out["gateway_state"] = (
            aws_sdk_mediaconnect.types.gateway_state.deserialize_json(
                data["gatewayState"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
