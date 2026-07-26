"""Generated from Smithy shape ``com.amazonaws.medialive#LastFrameClippingBehavior``."""

from typing import Literal, TypeAlias, cast

"""If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode."""
LastFrameClippingBehavior: TypeAlias = Literal[
    "EXCLUDE_LAST_FRAME",
    "INCLUDE_LAST_FRAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: LastFrameClippingBehavior) -> str:
    return value


def deserialize_json(data: str) -> LastFrameClippingBehavior:
    return cast(LastFrameClippingBehavior, data)
