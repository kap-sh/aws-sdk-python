"""Generated from Smithy shape ``com.amazonaws.glue#LimitedStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_limited_string

LimitedStringList: TypeAlias = list[
    "aws_sdk_glue.types.generic_limited_string.GenericLimitedString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitedStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LimitedStringList:
    return list(data)
