"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageFilterName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AnalyticsIntentStageFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentStageFilterName:
    return cast(AnalyticsIntentStageFilterName, data)
