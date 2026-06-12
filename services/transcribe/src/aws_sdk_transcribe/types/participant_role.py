"""Generated from Smithy shape ``com.amazonaws.transcribe#ParticipantRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

ParticipantRole: TypeAlias = Literal[
    "AGENT",
    "CUSTOMER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGENT",
        "CUSTOMER",
    )
)


def serialize_aws_json_1_1(value: ParticipantRole) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParticipantRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantRole value: {data!r}")
    return cast(ParticipantRole, data)
