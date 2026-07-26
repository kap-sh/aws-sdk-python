"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewaymanagementapi.types.__string


class DeleteConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_apigatewaymanagementapi.types.__string.__string"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
