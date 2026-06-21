"""Generated from Smithy shape ``com.amazonaws.wafv2#FieldToProtectType``."""

from typing import Literal, TypeAlias, cast

FieldToProtectType: TypeAlias = Literal[
    "SINGLE_HEADER",
    "SINGLE_COOKIE",
    "SINGLE_QUERY_ARGUMENT",
    "QUERY_STRING",
    "BODY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldToProtectType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldToProtectType:
    return cast(FieldToProtectType, data)
