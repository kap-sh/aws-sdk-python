"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#HandshakeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

HandshakeType: TypeAlias = Literal[
    "START_SERVICE_PERIOD",
    "REVOKE_SERVICE_PERIOD",
    "PROGRAM_MANAGEMENT_ACCOUNT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_SERVICE_PERIOD",
        "REVOKE_SERVICE_PERIOD",
        "PROGRAM_MANAGEMENT_ACCOUNT",
    )
)


def serialize_aws_json_1_0(value: HandshakeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HandshakeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HandshakeType value: {data!r}")
    return cast(HandshakeType, data)
