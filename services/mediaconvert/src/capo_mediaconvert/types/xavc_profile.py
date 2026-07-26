"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcProfile``."""

from typing import Literal, TypeAlias, cast

"""Specify the XAVC profile for this output. For more information, see the Sony documentation at https://www.xavc-info.org/. Note that MediaConvert doesn't support the interlaced video XAVC operating points for XAVC_HD_INTRA_CBG. To create an interlaced XAVC output, choose the profile XAVC_HD."""
XavcProfile: TypeAlias = Literal[
    "XAVC_HD_INTRA_CBG",
    "XAVC_4K_INTRA_CBG",
    "XAVC_4K_INTRA_VBR",
    "XAVC_HD",
    "XAVC_4K",
]


# --- restJson1 ser/de ---
def serialize_json(value: XavcProfile) -> str:
    return value


def deserialize_json(data: str) -> XavcProfile:
    return cast(XavcProfile, data)
