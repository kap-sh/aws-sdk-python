"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSourceType``."""

from typing import Literal, TypeAlias, cast

"""Use Source to identify the format of your input captions. The service cannot auto-detect caption format."""
CaptionSourceType: TypeAlias = Literal[
    "ANCILLARY",
    "DVB_SUB",
    "EMBEDDED",
    "SCTE20",
    "SCC",
    "TTML",
    "STL",
    "SRT",
    "SMI",
    "SMPTE_TT",
    "TELETEXT",
    "NULL_SOURCE",
    "IMSC",
    "WEBVTT",
    "TT_3GPP",
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSourceType) -> str:
    return value


def deserialize_json(data: str) -> CaptionSourceType:
    return cast(CaptionSourceType, data)
