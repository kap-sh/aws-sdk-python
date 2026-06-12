"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: CaptionSourceType) -> str:
    return value


def deserialize_json(data: str) -> CaptionSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CaptionSourceType value: {data!r}")
    return cast(CaptionSourceType, data)
