"""Generated from Smithy shape ``com.amazonaws.connect#InstanceStorageResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

InstanceStorageResourceType: TypeAlias = Literal[
    "CHAT_TRANSCRIPTS",
    "CALL_RECORDINGS",
    "SCHEDULED_REPORTS",
    "MEDIA_STREAMS",
    "CONTACT_TRACE_RECORDS",
    "AGENT_EVENTS",
    "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
    "ATTACHMENTS",
    "CONTACT_EVALUATIONS",
    "SCREEN_RECORDINGS",
    "REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS",
    "REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS",
    "EMAIL_MESSAGES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHAT_TRANSCRIPTS",
        "CALL_RECORDINGS",
        "SCHEDULED_REPORTS",
        "MEDIA_STREAMS",
        "CONTACT_TRACE_RECORDS",
        "AGENT_EVENTS",
        "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
        "ATTACHMENTS",
        "CONTACT_EVALUATIONS",
        "SCREEN_RECORDINGS",
        "REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS",
        "REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS",
        "EMAIL_MESSAGES",
    )
)


def serialize_json(value: InstanceStorageResourceType) -> str:
    return value


def deserialize_json(data: str) -> InstanceStorageResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceStorageResourceType value: {data!r}"
        )
    return cast(InstanceStorageResourceType, data)
