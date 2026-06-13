"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentVariantValues``."""

from typing import TypeAlias

ComponentVariantValues: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentVariantValues) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ComponentVariantValues:
    out: ComponentVariantValues = {}
    for key, value in data.items():
        out[key] = value
    return out
