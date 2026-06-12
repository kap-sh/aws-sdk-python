"""Generated from Smithy shape ``com.amazonaws.glue#FieldFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

FieldFilterOperator: TypeAlias = Literal[
    "LESS_THAN",
    "GREATER_THAN",
    "BETWEEN",
    "EQUAL_TO",
    "NOT_EQUAL_TO",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN_OR_EQUAL_TO",
    "CONTAINS",
    "ORDER_BY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LESS_THAN",
        "GREATER_THAN",
        "BETWEEN",
        "EQUAL_TO",
        "NOT_EQUAL_TO",
        "GREATER_THAN_OR_EQUAL_TO",
        "LESS_THAN_OR_EQUAL_TO",
        "CONTAINS",
        "ORDER_BY",
    )
)


def serialize_aws_json_1_1(value: FieldFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldFilterOperator value: {data!r}")
    return cast(FieldFilterOperator, data)
