"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationAlgorithm``."""

from typing import Literal, TypeAlias, cast

"""Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1."""
AudioNormalizationAlgorithm: TypeAlias = Literal[
    "ITU_BS_1770_1",
    "ITU_BS_1770_2",
    "ITU_BS_1770_3",
    "ITU_BS_1770_4",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationAlgorithm:
    return cast(AudioNormalizationAlgorithm, data)
