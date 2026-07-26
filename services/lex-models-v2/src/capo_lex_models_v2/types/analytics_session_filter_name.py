"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionFilterName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AnalyticsSessionFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionFilterName:
    return cast(AnalyticsSessionFilterName, data)
