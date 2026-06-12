"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_contacts.errors import DeserializationError

ChannelType: TypeAlias = Literal[
    "SMS",
    "VOICE",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMS",
        "VOICE",
        "EMAIL",
    )
)


def serialize_aws_json_1_1(value: ChannelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelType value: {data!r}")
    return cast(ChannelType, data)
