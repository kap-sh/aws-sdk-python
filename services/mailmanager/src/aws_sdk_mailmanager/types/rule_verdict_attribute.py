"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleVerdictAttribute: TypeAlias = Literal[
    "SPF",
    "DKIM",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPF",
        "DKIM",
    )
)


def serialize_aws_json_1_0(value: RuleVerdictAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleVerdictAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleVerdictAttribute value: {data!r}")
    return cast(RuleVerdictAttribute, data)
