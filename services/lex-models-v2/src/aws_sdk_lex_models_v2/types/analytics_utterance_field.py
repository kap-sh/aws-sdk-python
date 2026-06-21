"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceField``."""

from typing import Literal, TypeAlias, cast

AnalyticsUtteranceField: TypeAlias = Literal[
    "UtteranceText",
    "UtteranceState",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceField:
    return cast(AnalyticsUtteranceField, data)
