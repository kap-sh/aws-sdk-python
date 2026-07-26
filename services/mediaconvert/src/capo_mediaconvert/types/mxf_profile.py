"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MxfProfile``."""

from typing import Literal, TypeAlias, cast

"""Specify the MXF profile, also called shim, for this output. To automatically select a profile according to your output video codec and resolution, leave blank. For a list of codecs supported with each MXF profile, see https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html. For more information about the automatic selection behavior, see https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html."""
MxfProfile: TypeAlias = Literal[
    "D_10",
    "XDCAM",
    "OP1A",
    "XAVC",
    "XDCAM_RDD9",
]


# --- restJson1 ser/de ---
def serialize_json(value: MxfProfile) -> str:
    return value


def deserialize_json(data: str) -> MxfProfile:
    return cast(MxfProfile, data)
