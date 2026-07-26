"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceAttributeName``."""

from typing import Literal, TypeAlias, cast

AnalyticsUtteranceAttributeName: TypeAlias = Literal["LastUsedIntent",]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceAttributeName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceAttributeName:
    return cast(AnalyticsUtteranceAttributeName, data)
