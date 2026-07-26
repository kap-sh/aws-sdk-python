"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageField``."""

from typing import Literal, TypeAlias, cast

AnalyticsIntentStageField: TypeAlias = Literal[
    "IntentStageName",
    "SwitchedToIntent",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageField) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsIntentStageField:
    return cast(AnalyticsIntentStageField, data)
