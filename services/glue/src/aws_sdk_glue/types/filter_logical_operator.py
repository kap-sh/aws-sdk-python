"""Generated from Smithy shape ``com.amazonaws.glue#FilterLogicalOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FilterLogicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "OR",
    )
)


def serialize_aws_json_1_1(value: FilterLogicalOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterLogicalOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterLogicalOperator value: {data!r}")
    return cast(FilterLogicalOperator, data)
