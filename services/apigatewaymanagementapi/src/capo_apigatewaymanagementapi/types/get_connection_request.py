"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#GetConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewaymanagementapi.types.__string


class GetConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_apigatewaymanagementapi.types.__string.__string"


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectionRequest:
    out: GetConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
