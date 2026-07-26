"""Generated from Smithy shape ``com.amazonaws.braket#HyperParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.string256

HyperParameters: TypeAlias = dict["capo_braket.types.string256.String256", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HyperParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> HyperParameters:
    out: HyperParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
