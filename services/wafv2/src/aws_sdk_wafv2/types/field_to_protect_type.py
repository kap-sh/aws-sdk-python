"""Generated from Smithy shape ``com.amazonaws.wafv2#FieldToProtectType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

FieldToProtectType: TypeAlias = Literal[
    "SINGLE_HEADER",
    "SINGLE_COOKIE",
    "SINGLE_QUERY_ARGUMENT",
    "QUERY_STRING",
    "BODY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_HEADER",
        "SINGLE_COOKIE",
        "SINGLE_QUERY_ARGUMENT",
        "QUERY_STRING",
        "BODY",
    )
)


def serialize_aws_json_1_1(value: FieldToProtectType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldToProtectType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldToProtectType value: {data!r}")
    return cast(FieldToProtectType, data)
