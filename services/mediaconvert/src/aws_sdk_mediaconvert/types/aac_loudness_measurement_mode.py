"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacLoudnessMeasurementMode``."""

from typing import Literal, TypeAlias, cast

"""Choose the loudness measurement mode for your audio content. For music or advertisements: We recommend that you keep the default value, Program. For speech or other content: We recommend that you choose Anchor. When you do, MediaConvert optimizes the loudness of your output for clarify by applying speech gates."""
AacLoudnessMeasurementMode: TypeAlias = Literal[
    "PROGRAM",
    "ANCHOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacLoudnessMeasurementMode) -> str:
    return value


def deserialize_json(data: str) -> AacLoudnessMeasurementMode:
    return cast(AacLoudnessMeasurementMode, data)
