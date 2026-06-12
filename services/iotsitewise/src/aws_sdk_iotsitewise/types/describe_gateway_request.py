"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class DescribeGatewayRequest(TypedDict):
    gateway_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the gateway device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGatewayRequest:
    out: DescribeGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
