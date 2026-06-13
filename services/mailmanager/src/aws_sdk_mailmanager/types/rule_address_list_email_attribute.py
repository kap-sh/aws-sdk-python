"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleAddressListEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleAddressListEmailAttribute: TypeAlias = Literal[
    "RECIPIENT",
    "MAIL_FROM",
    "SENDER",
    "FROM",
    "TO",
    "CC",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RECIPIENT",
        "MAIL_FROM",
        "SENDER",
        "FROM",
        "TO",
        "CC",
    )
)


def serialize_aws_json_1_0(value: RuleAddressListEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleAddressListEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RuleAddressListEmailAttribute value: {data!r}"
        )
    return cast(RuleAddressListEmailAttribute, data)
