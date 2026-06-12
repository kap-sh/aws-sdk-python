"""Generated from Smithy shape ``com.amazonaws.connect#IntegrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

IntegrationType: TypeAlias = Literal[
    "EVENT",
    "VOICE_ID",
    "PINPOINT_APP",
    "WISDOM_ASSISTANT",
    "WISDOM_KNOWLEDGE_BASE",
    "WISDOM_QUICK_RESPONSES",
    "Q_MESSAGE_TEMPLATES",
    "CASES_DOMAIN",
    "APPLICATION",
    "FILE_SCANNER",
    "SES_IDENTITY",
    "ANALYTICS_CONNECTOR",
    "CALL_TRANSFER_CONNECTOR",
    "COGNITO_USER_POOL",
    "MESSAGE_PROCESSOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENT",
        "VOICE_ID",
        "PINPOINT_APP",
        "WISDOM_ASSISTANT",
        "WISDOM_KNOWLEDGE_BASE",
        "WISDOM_QUICK_RESPONSES",
        "Q_MESSAGE_TEMPLATES",
        "CASES_DOMAIN",
        "APPLICATION",
        "FILE_SCANNER",
        "SES_IDENTITY",
        "ANALYTICS_CONNECTOR",
        "CALL_TRANSFER_CONNECTOR",
        "COGNITO_USER_POOL",
        "MESSAGE_PROCESSOR",
    )
)


def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationType value: {data!r}")
    return cast(IntegrationType, data)
