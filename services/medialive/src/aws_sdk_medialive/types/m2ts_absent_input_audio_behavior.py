"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAbsentInputAudioBehavior``."""

from typing import Literal, TypeAlias, cast

"""M2ts Absent Input Audio Behavior"""
M2tsAbsentInputAudioBehavior: TypeAlias = Literal[
    "DROP",
    "ENCODE_SILENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsAbsentInputAudioBehavior) -> str:
    return value


def deserialize_json(data: str) -> M2tsAbsentInputAudioBehavior:
    return cast(M2tsAbsentInputAudioBehavior, data)
