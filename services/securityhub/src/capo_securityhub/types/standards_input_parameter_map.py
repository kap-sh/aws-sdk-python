"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsInputParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string

StandardsInputParameterMap: TypeAlias = dict[
    "capo_securityhub.types.non_empty_string.NonEmptyString",
    "capo_securityhub.types.non_empty_string.NonEmptyString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StandardsInputParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StandardsInputParameterMap:
    out: StandardsInputParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
