"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssociatedTranscriptFilterName``."""

from typing import Literal, TypeAlias, cast

AssociatedTranscriptFilterName: TypeAlias = Literal[
    "IntentId",
    "SlotTypeId",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTranscriptFilterName) -> str:
    return value


def deserialize_json(data: str) -> AssociatedTranscriptFilterName:
    return cast(AssociatedTranscriptFilterName, data)
