"""Generated from Smithy shape ``com.amazonaws.emr#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "GREATER_THAN_OR_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_THAN_OR_EQUAL",
        "GREATER_THAN",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
    )
)


def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
