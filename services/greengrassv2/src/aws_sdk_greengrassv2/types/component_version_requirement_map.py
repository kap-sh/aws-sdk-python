"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentVersionRequirementMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.non_empty_string

ComponentVersionRequirementMap: TypeAlias = dict[
    "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString",
    "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentVersionRequirementMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ComponentVersionRequirementMap:
    out: ComponentVersionRequirementMap = {}
    for key, value in data.items():
        out[key] = value
    return out
