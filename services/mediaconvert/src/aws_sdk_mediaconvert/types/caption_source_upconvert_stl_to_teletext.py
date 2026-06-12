"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSourceUpconvertSTLToTeletext``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether this set of input captions appears in your outputs in both STL and Teletext format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the STL data through using the Teletext compatibility bytes fields of the Teletext wrapper, and it also translates the STL data into Teletext."""
CaptionSourceUpconvertSTLToTeletext: TypeAlias = Literal[
    "UPCONVERT",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPCONVERT",
        "DISABLED",
    )
)


def serialize_json(value: CaptionSourceUpconvertSTLToTeletext) -> str:
    return value


def deserialize_json(data: str) -> CaptionSourceUpconvertSTLToTeletext:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CaptionSourceUpconvertSTLToTeletext value: {data!r}"
        )
    return cast(CaptionSourceUpconvertSTLToTeletext, data)
