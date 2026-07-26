"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentFilterName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AnalyticsIntentFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentFilterName:
    return cast(AnalyticsIntentFilterName, data)
