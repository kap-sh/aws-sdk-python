"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakePartyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

HandshakePartyType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "ORGANIZATION",
        "EMAIL",
    )
)


def serialize_aws_json_1_1(value: HandshakePartyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HandshakePartyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HandshakePartyType value: {data!r}")
    return cast(HandshakePartyType, data)
