"""Generated from Smithy shape ``com.amazonaws.greengrassv2#StringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.non_empty_string

StringMap: TypeAlias = dict[
    "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString",
    "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StringMap:
    out: StringMap = {}
    for key, value in data.items():
        out[key] = value
    return out
