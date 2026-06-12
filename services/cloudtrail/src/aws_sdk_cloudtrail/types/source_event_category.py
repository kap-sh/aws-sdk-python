"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SourceEventCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

SourceEventCategory: TypeAlias = Literal[
    "Management",
    "Data",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Management",
        "Data",
    )
)


def serialize_aws_json_1_1(value: SourceEventCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceEventCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceEventCategory value: {data!r}")
    return cast(SourceEventCategory, data)
