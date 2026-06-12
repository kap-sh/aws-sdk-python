"""Generated from Smithy shape ``com.amazonaws.qapps#PresignedUrlFields``."""

from typing import TypeAlias

PresignedUrlFields: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PresignedUrlFields) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PresignedUrlFields:
    out: PresignedUrlFields = {}
    for key, value in data.items():
        out[key] = value
    return out
