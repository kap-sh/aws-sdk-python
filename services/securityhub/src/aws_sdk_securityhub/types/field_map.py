"""Generated from Smithy shape ``com.amazonaws.securityhub#FieldMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string

FieldMap: TypeAlias = dict[
    "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
    "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FieldMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FieldMap:
    out: FieldMap = {}
    for key, value in data.items():
        out[key] = value
    return out
