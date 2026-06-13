"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeGatewayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.gateway


class DescribeGatewayResponse(TypedDict):
    gateway: NotRequired["aws_sdk_mediaconnect.types.gateway.Gateway"]
    """<p>The gateway that you wanted to describe. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayResponse) -> dict:
    out: dict = {}
    if "gateway" in value:
        import aws_sdk_mediaconnect.types.gateway

        out["gateway"] = aws_sdk_mediaconnect.types.gateway.serialize_json(
            value["gateway"]
        )
    return out


def deserialize_json(data: dict) -> DescribeGatewayResponse:
    out: DescribeGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gateway" in data:
        import aws_sdk_mediaconnect.types.gateway

        out["gateway"] = aws_sdk_mediaconnect.types.gateway.deserialize_json(
            data["gateway"]
        )
    return out
