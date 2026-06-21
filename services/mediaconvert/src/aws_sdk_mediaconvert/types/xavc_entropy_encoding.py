"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcEntropyEncoding``."""

from typing import Literal, TypeAlias, cast

"""Optional. Choose a specific entropy encoding mode only when you want to override XAVC recommendations. If you choose the value auto, MediaConvert uses the mode that the XAVC file format specifies given this output's operating point."""
XavcEntropyEncoding: TypeAlias = Literal[
    "AUTO",
    "CABAC",
    "CAVLC",
]


# --- restJson1 ser/de ---
def serialize_json(value: XavcEntropyEncoding) -> str:
    return value


def deserialize_json(data: str) -> XavcEntropyEncoding:
    return cast(XavcEntropyEncoding, data)
