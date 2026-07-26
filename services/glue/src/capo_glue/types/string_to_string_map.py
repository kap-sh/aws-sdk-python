"""Generated from Smithy shape ``com.amazonaws.glue#StringToStringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.nullable_string

StringToStringMap: TypeAlias = dict[
    "capo_glue.types.nullable_string.NullableString",
    "capo_glue.types.nullable_string.NullableString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: StringToStringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> StringToStringMap:
    out: StringToStringMap = {}
    for key, value in data.items():
        out[key] = value
    return out
