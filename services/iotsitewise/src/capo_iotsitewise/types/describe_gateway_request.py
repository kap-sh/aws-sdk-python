"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class DescribeGatewayRequest(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGatewayRequest:
    out: DescribeGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
