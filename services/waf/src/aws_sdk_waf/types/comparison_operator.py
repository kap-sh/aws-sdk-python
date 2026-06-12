"""Generated from Smithy shape ``com.amazonaws.waf#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "EQ",
    "NE",
    "LE",
    "LT",
    "GE",
    "GT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "NE",
        "LE",
        "LT",
        "GE",
        "GT",
    )
)


def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
