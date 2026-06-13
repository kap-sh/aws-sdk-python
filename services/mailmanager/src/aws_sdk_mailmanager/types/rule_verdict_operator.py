"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleVerdictOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
    )
)


def serialize_aws_json_1_0(value: RuleVerdictOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleVerdictOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleVerdictOperator value: {data!r}")
    return cast(RuleVerdictOperator, data)
