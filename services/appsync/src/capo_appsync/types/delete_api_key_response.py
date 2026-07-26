"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteApiKeyResponse``."""

from typing_extensions import TypedDict


class DeleteApiKeyResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApiKeyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApiKeyResponse:
    out: DeleteApiKeyResponse = {}  # type: ignore[typeddict-item]
    return out
