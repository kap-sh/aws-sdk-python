"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.gateway_arn


class DescribeGatewayRequest(TypedDict, closed=True):
    gateway_arn: "aws_sdk_mediaconnect.types.gateway_arn.GatewayArn"
    """<p> The ARN of the gateway that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGatewayRequest:
    out: DescribeGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
