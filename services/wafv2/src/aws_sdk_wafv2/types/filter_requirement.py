"""Generated from Smithy shape ``com.amazonaws.wafv2#FilterRequirement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

FilterRequirement: TypeAlias = Literal[
    "MEETS_ALL",
    "MEETS_ANY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MEETS_ALL",
        "MEETS_ANY",
    )
)


def serialize_aws_json_1_1(value: FilterRequirement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterRequirement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterRequirement value: {data!r}")
    return cast(FilterRequirement, data)
