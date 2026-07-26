"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MxfUncompressedAudioWrapping``."""

from typing import Literal, TypeAlias, cast

"""Choose the audio frame wrapping mode for PCM tracks in MXF outputs. AUTO (default): Uses codec-appropriate defaults - BWF for H.264/AVC, AES3 for MPEG2/XDCAM. AES3: Use AES3 frame wrapping with SMPTE-compliant descriptors. This setting only takes effect when the MXF profile is OP1a."""
MxfUncompressedAudioWrapping: TypeAlias = Literal[
    "AUTO",
    "AES3",
]


# --- restJson1 ser/de ---
def serialize_json(value: MxfUncompressedAudioWrapping) -> str:
    return value


def deserialize_json(data: str) -> MxfUncompressedAudioWrapping:
    return cast(MxfUncompressedAudioWrapping, data)
