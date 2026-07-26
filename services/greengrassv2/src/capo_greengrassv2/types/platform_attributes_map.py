"""Generated from Smithy shape ``com.amazonaws.greengrassv2#PlatformAttributesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.non_empty_string

PlatformAttributesMap: TypeAlias = dict[
    "capo_greengrassv2.types.non_empty_string.NonEmptyString",
    "capo_greengrassv2.types.non_empty_string.NonEmptyString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PlatformAttributesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PlatformAttributesMap:
    out: PlatformAttributesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
