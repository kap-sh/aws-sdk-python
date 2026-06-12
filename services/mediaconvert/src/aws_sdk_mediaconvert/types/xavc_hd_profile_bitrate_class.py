"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdProfileBitrateClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
XavcHdProfileBitrateClass: TypeAlias = Literal[
    "BITRATE_CLASS_25",
    "BITRATE_CLASS_35",
    "BITRATE_CLASS_50",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BITRATE_CLASS_25",
        "BITRATE_CLASS_35",
        "BITRATE_CLASS_50",
    )
)


def serialize_json(value: XavcHdProfileBitrateClass) -> str:
    return value


def deserialize_json(data: str) -> XavcHdProfileBitrateClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown XavcHdProfileBitrateClass value: {data!r}")
    return cast(XavcHdProfileBitrateClass, data)
