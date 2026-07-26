"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteCodeSigningConfigResponse``."""

from typing_extensions import TypedDict


class DeleteCodeSigningConfigResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeSigningConfigResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCodeSigningConfigResponse:
    out: DeleteCodeSigningConfigResponse = {}  # type: ignore[typeddict-item]
    return out
