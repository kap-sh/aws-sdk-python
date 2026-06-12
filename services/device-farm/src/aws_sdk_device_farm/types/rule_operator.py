"""Generated from Smithy shape ``com.amazonaws.devicefarm#RuleOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

RuleOperator: TypeAlias = Literal[
    "EQUALS",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "IN",
    "NOT_IN",
    "CONTAINS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "LESS_THAN",
        "LESS_THAN_OR_EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUALS",
        "IN",
        "NOT_IN",
        "CONTAINS",
    )
)


def serialize_aws_json_1_1(value: RuleOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleOperator value: {data!r}")
    return cast(RuleOperator, data)
