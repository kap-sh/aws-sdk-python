"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class DeleteGatewayRequest(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayRequest:
    out: DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
