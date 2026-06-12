"""Generated from Smithy shape ``com.amazonaws.servicediscovery#FilterCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

FilterCondition: TypeAlias = Literal[
    "EQ",
    "IN",
    "BETWEEN",
    "BEGINS_WITH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "IN",
        "BETWEEN",
        "BEGINS_WITH",
    )
)


def serialize_aws_json_1_1(value: FilterCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterCondition value: {data!r}")
    return cast(FilterCondition, data)
