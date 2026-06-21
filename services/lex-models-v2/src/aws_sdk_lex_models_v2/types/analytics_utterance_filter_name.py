"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceFilterName``."""

from typing import Literal, TypeAlias, cast

AnalyticsUtteranceFilterName: TypeAlias = Literal[
    "BotAliasId",
    "BotVersion",
    "LocaleId",
    "Modality",
    "Channel",
    "SessionId",
    "OriginatingRequestId",
    "UtteranceState",
    "UtteranceText",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceFilterName:
    return cast(AnalyticsUtteranceFilterName, data)
