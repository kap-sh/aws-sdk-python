"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AutomaticEncryptionKeyConfiguration``."""

from typing_extensions import TypedDict


class AutomaticEncryptionKeyConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AutomaticEncryptionKeyConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AutomaticEncryptionKeyConfiguration:
    out: AutomaticEncryptionKeyConfiguration = {}  # type: ignore[typeddict-item]
    return out
