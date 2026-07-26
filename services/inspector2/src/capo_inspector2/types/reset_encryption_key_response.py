"""Generated from Smithy shape ``com.amazonaws.inspector2#ResetEncryptionKeyResponse``."""

from typing_extensions import TypedDict


class ResetEncryptionKeyResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ResetEncryptionKeyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResetEncryptionKeyResponse:
    out: ResetEncryptionKeyResponse = {}  # type: ignore[typeddict-item]
    return out
