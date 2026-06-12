"""Generated from Smithy shape ``com.amazonaws.iot#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "less-than",
    "less-than-equals",
    "greater-than",
    "greater-than-equals",
    "in-cidr-set",
    "not-in-cidr-set",
    "in-port-set",
    "not-in-port-set",
    "in-set",
    "not-in-set",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "less-than",
        "less-than-equals",
        "greater-than",
        "greater-than-equals",
        "in-cidr-set",
        "not-in-cidr-set",
        "in-port-set",
        "not-in-port-set",
        "in-set",
        "not-in-set",
    )
)


def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
