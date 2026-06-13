"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleStringOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
        "STARTS_WITH",
        "ENDS_WITH",
        "CONTAINS",
    )
)


def serialize_aws_json_1_0(value: RuleStringOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleStringOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleStringOperator value: {data!r}")
    return cast(RuleStringOperator, data)
