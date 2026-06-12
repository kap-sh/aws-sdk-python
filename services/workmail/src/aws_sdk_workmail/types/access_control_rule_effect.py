"""Generated from Smithy shape ``com.amazonaws.workmail#AccessControlRuleEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

AccessControlRuleEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_1(value: AccessControlRuleEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessControlRuleEffect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessControlRuleEffect value: {data!r}")
    return cast(AccessControlRuleEffect, data)
