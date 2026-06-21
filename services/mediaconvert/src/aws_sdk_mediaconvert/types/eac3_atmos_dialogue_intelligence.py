"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosDialogueIntelligence``."""

from typing import Literal, TypeAlias, cast

"""Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis."""
Eac3AtmosDialogueIntelligence: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosDialogueIntelligence) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDialogueIntelligence:
    return cast(Eac3AtmosDialogueIntelligence, data)
