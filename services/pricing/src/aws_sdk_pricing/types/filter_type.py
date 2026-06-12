"""Generated from Smithy shape ``com.amazonaws.pricing#FilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pricing.errors import DeserializationError

FilterType: TypeAlias = Literal[
    "TERM_MATCH",
    "EQUALS",
    "CONTAINS",
    "ANY_OF",
    "NONE_OF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TERM_MATCH",
        "EQUALS",
        "CONTAINS",
        "ANY_OF",
        "NONE_OF",
    )
)


def serialize_aws_json_1_1(value: FilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterType value: {data!r}")
    return cast(FilterType, data)
