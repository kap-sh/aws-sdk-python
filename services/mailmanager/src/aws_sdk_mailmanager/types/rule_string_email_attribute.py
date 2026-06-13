"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleStringEmailAttribute: TypeAlias = Literal[
    "MAIL_FROM",
    "HELO",
    "RECIPIENT",
    "SENDER",
    "FROM",
    "SUBJECT",
    "TO",
    "CC",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAIL_FROM",
        "HELO",
        "RECIPIENT",
        "SENDER",
        "FROM",
        "SUBJECT",
        "TO",
        "CC",
    )
)


def serialize_aws_json_1_0(value: RuleStringEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleStringEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleStringEmailAttribute value: {data!r}")
    return cast(RuleStringEmailAttribute, data)
