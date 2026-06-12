"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsIntentStageFilterName: TypeAlias = Literal[
    "BotAliasId",
    "BotVersion",
    "LocaleId",
    "Modality",
    "Channel",
    "SessionId",
    "OriginatingRequestId",
    "IntentName",
    "IntentStageName",
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
        "IntentStageName",
    )
)


def serialize_json(value: AnalyticsIntentStageFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentStageFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsIntentStageFilterName value: {data!r}"
        )
    return cast(AnalyticsIntentStageFilterName, data)
