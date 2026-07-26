"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#KMSEncryptionContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.non_empty_string

KMSEncryptionContextMap: TypeAlias = dict[
    "capo_transcribe_streaming.types.non_empty_string.NonEmptyString",
    "capo_transcribe_streaming.types.non_empty_string.NonEmptyString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: KMSEncryptionContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> KMSEncryptionContextMap:
    out: KMSEncryptionContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
