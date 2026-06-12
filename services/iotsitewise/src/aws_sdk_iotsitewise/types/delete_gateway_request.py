"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class DeleteGatewayRequest(TypedDict):
    gateway_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the gateway to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayRequest:
    out: DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
