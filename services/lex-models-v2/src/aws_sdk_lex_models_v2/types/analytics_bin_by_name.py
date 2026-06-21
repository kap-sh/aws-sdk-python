"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsBinByName``."""

from typing import Literal, TypeAlias, cast

AnalyticsBinByName: TypeAlias = Literal[
    "ConversationStartTime",
    "UtteranceTimestamp",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsBinByName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsBinByName:
    return cast(AnalyticsBinByName, data)
