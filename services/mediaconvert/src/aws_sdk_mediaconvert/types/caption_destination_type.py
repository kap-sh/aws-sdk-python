"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionDestinationType``."""

from typing import Literal, TypeAlias, cast

"""Specify the format for this set of captions on this output. The default format is embedded without SCTE-20. Note that your choice of video output container constrains your choice of output captions format. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/captions-support-tables.html. If you are using SCTE-20 and you want to create an output that complies with the SCTE-43 spec, choose SCTE-20 plus embedded. To create a non-compliant output where the embedded captions come first, choose Embedded plus SCTE-20."""
CaptionDestinationType: TypeAlias = Literal[
    "BURN_IN",
    "DVB_SUB",
    "EMBEDDED",
    "EMBEDDED_PLUS_SCTE20",
    "IMSC",
    "SCTE20_PLUS_EMBEDDED",
    "SCC",
    "SRT",
    "SMI",
    "TELETEXT",
    "TTML",
    "WEBVTT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionDestinationType) -> str:
    return value


def deserialize_json(data: str) -> CaptionDestinationType:
    return cast(CaptionDestinationType, data)
