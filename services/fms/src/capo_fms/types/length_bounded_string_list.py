"""Generated from Smithy shape ``com.amazonaws.fms#LengthBoundedStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string

LengthBoundedStringList: TypeAlias = list[
    "capo_fms.types.length_bounded_string.LengthBoundedString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LengthBoundedStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LengthBoundedStringList:
    return list(data)
