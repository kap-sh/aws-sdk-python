"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionField``."""

from typing import Literal, TypeAlias, cast

AnalyticsSessionField: TypeAlias = Literal[
    "ConversationEndState",
    "LocaleId",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSessionField:
    return cast(AnalyticsSessionField, data)
