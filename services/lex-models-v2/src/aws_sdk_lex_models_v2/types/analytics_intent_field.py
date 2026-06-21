"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentField``."""

from typing import Literal, TypeAlias, cast

AnalyticsIntentField: TypeAlias = Literal[
    "IntentName",
    "IntentEndState",
    "IntentLevel",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentField:
    return cast(AnalyticsIntentField, data)
