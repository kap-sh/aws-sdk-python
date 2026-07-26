"""Generated from Smithy shape ``com.amazonaws.xray#GetEncryptionConfigRequest``."""

from typing_extensions import TypedDict


class GetEncryptionConfigRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetEncryptionConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEncryptionConfigRequest:
    out: GetEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
    return out
