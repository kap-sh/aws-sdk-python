"""Generated from Smithy shape ``com.amazonaws.datazone#TriggerSourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of trigger source for a notebook run in Amazon SageMaker Unified Studio.</p>"""
TriggerSourceType: TypeAlias = Literal[
    "MANUAL",
    "SCHEDULED",
    "WORKFLOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerSourceType) -> str:
    return value


def deserialize_json(data: str) -> TriggerSourceType:
    return cast(TriggerSourceType, data)
