"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewaymanagementapi.types.__string


class DeleteConnectionRequest(TypedDict):
    connection_id: "aws_sdk_apigatewaymanagementapi.types.__string.__string"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
