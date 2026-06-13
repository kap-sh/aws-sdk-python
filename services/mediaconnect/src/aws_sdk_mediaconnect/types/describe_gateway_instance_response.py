"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeGatewayInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.gateway_instance


class DescribeGatewayInstanceResponse(TypedDict):
    gateway_instance: NotRequired[
        "aws_sdk_mediaconnect.types.gateway_instance.GatewayInstance"
    ]
    """<p>The gateway instance that you requested a description of. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayInstanceResponse) -> dict:
    out: dict = {}
    if "gateway_instance" in value:
        import aws_sdk_mediaconnect.types.gateway_instance

        out["gatewayInstance"] = (
            aws_sdk_mediaconnect.types.gateway_instance.serialize_json(
                value["gateway_instance"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeGatewayInstanceResponse:
    out: DescribeGatewayInstanceResponse = {}  # type: ignore[typeddict-item]
    if "gatewayInstance" in data:
        import aws_sdk_mediaconnect.types.gateway_instance

        out["gateway_instance"] = (
            aws_sdk_mediaconnect.types.gateway_instance.deserialize_json(
                data["gatewayInstance"]
            )
        )
    return out
