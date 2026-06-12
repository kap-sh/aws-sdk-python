"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ParticipantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

ParticipantType: TypeAlias = Literal[
    "SENDER",
    "RECEIVER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SENDER",
        "RECEIVER",
    )
)


def serialize_aws_json_1_0(value: ParticipantType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ParticipantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantType value: {data!r}")
    return cast(ParticipantType, data)
