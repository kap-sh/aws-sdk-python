"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeGatewayInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.gateway_instance_arn


class DescribeGatewayInstanceRequest(TypedDict, closed=True):
    gateway_instance_arn: (
        "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn"
    )
    """<p> The Amazon Resource Name (ARN) of the gateway instance that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGatewayInstanceRequest:
    out: DescribeGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
