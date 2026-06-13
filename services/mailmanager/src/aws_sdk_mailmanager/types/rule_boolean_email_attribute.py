"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleBooleanEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleBooleanEmailAttribute: TypeAlias = Literal[
    "READ_RECEIPT_REQUESTED",
    "TLS",
    "TLS_WRAPPED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ_RECEIPT_REQUESTED",
        "TLS",
        "TLS_WRAPPED",
    )
)


def serialize_aws_json_1_0(value: RuleBooleanEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleBooleanEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleBooleanEmailAttribute value: {data!r}")
    return cast(RuleBooleanEmailAttribute, data)
