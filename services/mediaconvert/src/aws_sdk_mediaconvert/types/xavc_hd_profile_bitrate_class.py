"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdProfileBitrateClass``."""

from typing import Literal, TypeAlias, cast

"""Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
XavcHdProfileBitrateClass: TypeAlias = Literal[
    "BITRATE_CLASS_25",
    "BITRATE_CLASS_35",
    "BITRATE_CLASS_50",
]


# --- restJson1 ser/de ---
def serialize_json(value: XavcHdProfileBitrateClass) -> str:
    return value


def deserialize_json(data: str) -> XavcHdProfileBitrateClass:
    return cast(XavcHdProfileBitrateClass, data)
