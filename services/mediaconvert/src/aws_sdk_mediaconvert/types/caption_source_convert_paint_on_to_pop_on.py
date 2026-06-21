"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSourceConvertPaintOnToPopOn``."""

from typing import Literal, TypeAlias, cast

"""Choose the presentation style of your input SCC captions. To use the same presentation style as your input: Keep the default value, Disabled. To convert paint-on captions to pop-on: Choose Enabled. We also recommend that you choose Enabled if you notice additional repeated lines in your output captions."""
CaptionSourceConvertPaintOnToPopOn: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSourceConvertPaintOnToPopOn) -> str:
    return value


def deserialize_json(data: str) -> CaptionSourceConvertPaintOnToPopOn:
    return cast(CaptionSourceConvertPaintOnToPopOn, data)
