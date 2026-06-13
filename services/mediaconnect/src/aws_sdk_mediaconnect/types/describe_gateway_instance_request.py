"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeGatewayInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.gateway_instance_arn


class DescribeGatewayInstanceRequest(TypedDict):
    gateway_instance_arn: (
        "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn"
    )
    """<p> The Amazon Resource Name (ARN) of the gateway instance that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGatewayInstanceRequest:
    out: DescribeGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
