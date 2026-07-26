"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsPreventBufferUnderflow``."""

from typing import Literal, TypeAlias, cast

"""Specify whether MediaConvert automatically attempts to prevent decoder buffer underflows in your transport stream output. Use if you are seeing decoder buffer underflows in your output and are unable to increase your transport stream's bitrate. For most workflows: We recommend that you keep the default value, Disabled. To prevent decoder buffer underflows in your output, when possible: Choose Enabled. Note that if MediaConvert prevents a decoder buffer underflow in your output, output video quality is reduced and your job will take longer to complete."""
M2tsPreventBufferUnderflow: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsPreventBufferUnderflow) -> str:
    return value


def deserialize_json(data: str) -> M2tsPreventBufferUnderflow:
    return cast(M2tsPreventBufferUnderflow, data)
