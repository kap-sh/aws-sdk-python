"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsSessionFilterName: TypeAlias = Literal[
    "BotAliasId",
    "BotVersion",
    "LocaleId",
    "Modality",
    "Channel",
    "Duration",
    "ConversationEndState",
    "SessionId",
    "OriginatingRequestId",
    "IntentPath",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BotAliasId",
        "BotVersion",
        "LocaleId",
        "Modality",
        "Channel",
        "Duration",
        "ConversationEndState",
        "SessionId",
        "OriginatingRequestId",
        "IntentPath",
    )
)


def serialize_json(value: AnalyticsSessionFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsSessionFilterName value: {data!r}"
        )
    return cast(AnalyticsSessionFilterName, data)
