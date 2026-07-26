"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264QualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

"""The Quality tuning level you choose represents a trade-off between the encoding speed of your job and the output video quality. For the fastest encoding speed at the cost of video quality: Choose Single pass. For a good balance between encoding speed and video quality: Leave blank or keep the default value Single pass HQ. For the best video quality, at the cost of encoding speed: Choose Multi pass HQ. MediaConvert performs an analysis pass on your input followed by an encoding pass. Outputs that use this feature incur pro-tier pricing."""
H264QualityTuningLevel: TypeAlias = Literal[
    "SINGLE_PASS",
    "SINGLE_PASS_HQ",
    "MULTI_PASS_HQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264QualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> H264QualityTuningLevel:
    return cast(H264QualityTuningLevel, data)
