"""Generated from Smithy shape ``com.amazonaws.wafv2#FilterBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

FilterBehavior: TypeAlias = Literal[
    "KEEP",
    "DROP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEEP",
        "DROP",
    )
)


def serialize_aws_json_1_1(value: FilterBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterBehavior value: {data!r}")
    return cast(FilterBehavior, data)
