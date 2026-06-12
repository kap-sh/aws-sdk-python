"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessageListType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

StructuredMessageListType: TypeAlias = Literal[
    "FIXED_CAPACITY",
    "DYNAMIC_UNBOUNDED_CAPACITY",
    "DYNAMIC_BOUNDED_CAPACITY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIXED_CAPACITY",
        "DYNAMIC_UNBOUNDED_CAPACITY",
        "DYNAMIC_BOUNDED_CAPACITY",
    )
)


def serialize_aws_json_1_0(value: StructuredMessageListType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StructuredMessageListType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StructuredMessageListType value: {data!r}")
    return cast(StructuredMessageListType, data)
