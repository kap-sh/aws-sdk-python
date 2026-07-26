"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AncillaryConvert608To708``."""

from typing import Literal, TypeAlias, cast

"""Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708."""
AncillaryConvert608To708: TypeAlias = Literal[
    "UPCONVERT",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AncillaryConvert608To708) -> str:
    return value


def deserialize_json(data: str) -> AncillaryConvert608To708:
    return cast(AncillaryConvert608To708, data)
