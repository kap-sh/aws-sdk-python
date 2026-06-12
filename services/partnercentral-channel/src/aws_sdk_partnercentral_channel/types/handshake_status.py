"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#HandshakeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

HandshakeStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    "CANCELED",
    "EXPIRED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACCEPTED",
        "REJECTED",
        "CANCELED",
        "EXPIRED",
    )
)


def serialize_aws_json_1_0(value: HandshakeStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HandshakeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HandshakeStatus value: {data!r}")
    return cast(HandshakeStatus, data)
