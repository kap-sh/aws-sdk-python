"""Generated from Smithy shape ``com.amazonaws.budgets#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

"""<p> The comparison operator of a notification. Currently, the service supports the following operators:</p> <p> <code>GREATER_THAN</code>, <code>LESS_THAN</code>, <code>EQUAL_TO</code> </p>"""
ComparisonOperator: TypeAlias = Literal[
    "GREATER_THAN",
    "LESS_THAN",
    "EQUAL_TO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_THAN",
        "LESS_THAN",
        "EQUAL_TO",
    )
)


def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
