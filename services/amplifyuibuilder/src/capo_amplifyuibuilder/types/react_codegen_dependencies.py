"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ReactCodegenDependencies``."""

from typing import TypeAlias

ReactCodegenDependencies: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ReactCodegenDependencies) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ReactCodegenDependencies:
    out: ReactCodegenDependencies = {}
    for key, value in data.items():
        out[key] = value
    return out
