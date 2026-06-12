"""Generated from Smithy shape ``com.amazonaws.glue#FilterOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FilterOperation: TypeAlias = Literal[
    "EQ",
    "LT",
    "GT",
    "LTE",
    "GTE",
    "REGEX",
    "ISNULL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "LT",
        "GT",
        "LTE",
        "GTE",
        "REGEX",
        "ISNULL",
    )
)


def serialize_aws_json_1_1(value: FilterOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterOperation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterOperation value: {data!r}")
    return cast(FilterOperation, data)
