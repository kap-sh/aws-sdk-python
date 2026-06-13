"""Generated from Smithy shape ``com.amazonaws.datazone#CredentialMap``."""

from typing import TypeAlias

CredentialMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CredentialMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CredentialMap:
    out: CredentialMap = {}
    for key, value in data.items():
        out[key] = value
    return out
