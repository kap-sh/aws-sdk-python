"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeGatewayInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.gateway_instance


class DescribeGatewayInstanceResponse(TypedDict, closed=True):
    gateway_instance: NotRequired[
        "capo_mediaconnect.types.gateway_instance.GatewayInstance"
    ]
    """<p>The gateway instance that you requested a description of. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayInstanceResponse) -> dict:
    out: dict = {}
    if "gateway_instance" in value:
        import capo_mediaconnect.types.gateway_instance

        out["gatewayInstance"] = (
            capo_mediaconnect.types.gateway_instance.serialize_json(
                value["gateway_instance"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeGatewayInstanceResponse:
    out: DescribeGatewayInstanceResponse = {}  # type: ignore[typeddict-item]
    if "gatewayInstance" in data:
        import capo_mediaconnect.types.gateway_instance

        out["gateway_instance"] = (
            capo_mediaconnect.types.gateway_instance.deserialize_json(
                data["gatewayInstance"]
            )
        )
    return out
