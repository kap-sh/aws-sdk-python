"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#StatusDetails``."""

from typing import TypeAlias

StatusDetails: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StatusDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StatusDetails:
    out: StatusDetails = {}
    for key, value in data.items():
        out[key] = value
    return out
