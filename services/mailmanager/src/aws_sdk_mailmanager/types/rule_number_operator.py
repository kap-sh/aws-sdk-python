"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleNumberOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleNumberOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "LESS_THAN",
    "GREATER_THAN",
    "LESS_THAN_OR_EQUAL",
    "GREATER_THAN_OR_EQUAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
        "LESS_THAN",
        "GREATER_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN_OR_EQUAL",
    )
)


def serialize_aws_json_1_0(value: RuleNumberOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleNumberOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleNumberOperator value: {data!r}")
    return cast(RuleNumberOperator, data)
