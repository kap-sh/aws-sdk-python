"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsCommonFilterName``."""

from typing import Literal, TypeAlias, cast

AnalyticsCommonFilterName: TypeAlias = Literal[
    "BotAliasId",
    "BotVersion",
    "LocaleId",
    "Modality",
    "Channel",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsCommonFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsCommonFilterName:
    return cast(AnalyticsCommonFilterName, data)
