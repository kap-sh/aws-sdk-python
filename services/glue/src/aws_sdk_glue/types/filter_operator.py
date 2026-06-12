"""Generated from Smithy shape ``com.amazonaws.glue#FilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FilterOperator: TypeAlias = Literal[
    "GT",
    "GE",
    "LT",
    "LE",
    "EQ",
    "NE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GT",
        "GE",
        "LT",
        "LE",
        "EQ",
        "NE",
    )
)


def serialize_aws_json_1_1(value: FilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterOperator value: {data!r}")
    return cast(FilterOperator, data)
