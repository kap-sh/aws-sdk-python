"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleIpOperator: TypeAlias = Literal[
    "CIDR_MATCHES",
    "NOT_CIDR_MATCHES",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CIDR_MATCHES",
        "NOT_CIDR_MATCHES",
    )
)


def serialize_aws_json_1_0(value: RuleIpOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleIpOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleIpOperator value: {data!r}")
    return cast(RuleIpOperator, data)
