"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceSortByName``."""

from typing import Literal, TypeAlias, cast

AnalyticsUtteranceSortByName: TypeAlias = Literal["UtteranceTimestamp",]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceSortByName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceSortByName:
    return cast(AnalyticsUtteranceSortByName, data)
