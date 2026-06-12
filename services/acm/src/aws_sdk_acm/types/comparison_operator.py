"""Generated from Smithy shape ``com.amazonaws.acm#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

"""<p>The comparison operator to use for string filters. Valid values are <code>CONTAINS</code> and <code>EQUALS</code>.</p>"""
ComparisonOperator: TypeAlias = Literal[
    "CONTAINS",
    "EQUALS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTAINS",
        "EQUALS",
    )
)


def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
