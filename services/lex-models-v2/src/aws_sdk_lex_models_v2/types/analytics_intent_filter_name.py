"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsIntentFilterName: TypeAlias = Literal[
    "BotAliasId",
    "BotVersion",
    "LocaleId",
    "Modality",
    "Channel",
    "SessionId",
    "OriginatingRequestId",
    "IntentName",
    "IntentEndState",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BotAliasId",
        "BotVersion",
        "LocaleId",
        "Modality",
        "Channel",
        "SessionId",
        "OriginatingRequestId",
        "IntentName",
        "IntentEndState",
    )
)


def serialize_json(value: AnalyticsIntentFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsIntentFilterName value: {data!r}")
    return cast(AnalyticsIntentFilterName, data)
