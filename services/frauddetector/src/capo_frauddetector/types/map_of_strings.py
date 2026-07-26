"""Generated from Smithy shape ``com.amazonaws.frauddetector#MapOfStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.string

MapOfStrings: TypeAlias = dict[
    "capo_frauddetector.types.string.string", "capo_frauddetector.types.string.string"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MapOfStrings) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> MapOfStrings:
    out: MapOfStrings = {}
    for key, value in data.items():
        out[key] = value
    return out
