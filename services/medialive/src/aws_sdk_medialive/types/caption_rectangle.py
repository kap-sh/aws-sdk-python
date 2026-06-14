"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionRectangle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double_min0_max100


class CaptionRectangle(TypedDict):
    height: NotRequired[
        "aws_sdk_medialive.types.__double_min0_max100.__doubleMin0Max100"
    ]
    r"""See the description in leftOffset. For height, specify the entire height of the rectangle as a percentage of the underlying frame height. For example, \\"80\\" means the rectangle height is 80% of the underlying frame height. The topOffset and rectangleHeight must add up to 100% or less. This field corresponds to tts:extent - Y in the TTML standard."""
    left_offset: NotRequired[
        "aws_sdk_medialive.types.__double_min0_max100.__doubleMin0Max100"
    ]
    r"""Applies only if you plan to convert these source captions to EBU-TT-D or TTML in an output. (Make sure to leave the default if you don't have either of these formats in the output.) You can define a display rectangle for the captions that is smaller than the underlying video frame. You define the rectangle by specifying the position of the left edge, top edge, bottom edge, and right edge of the rectangle, all within the underlying video frame. The units for the measurements are percentages. If you specify a value for one of these fields, you must specify a value for all of them. For leftOffset, specify the position of the left edge of the rectangle, as a percentage of the underlying frame width, and relative to the left edge of the frame. For example, \\"10\\" means the measurement is 10% of the underlying frame width. The rectangle left edge starts at that position from the left edge of the frame. This field corresponds to tts:origin - X in the TTML standard."""
    top_offset: NotRequired[
        "aws_sdk_medialive.types.__double_min0_max100.__doubleMin0Max100"
    ]
    r"""See the description in leftOffset. For topOffset, specify the position of the top edge of the rectangle, as a percentage of the underlying frame height, and relative to the top edge of the frame. For example, \\"10\\" means the measurement is 10% of the underlying frame height. The rectangle top edge starts at that position from the top edge of the frame. This field corresponds to tts:origin - Y in the TTML standard."""
    width: NotRequired[
        "aws_sdk_medialive.types.__double_min0_max100.__doubleMin0Max100"
    ]
    r"""See the description in leftOffset. For width, specify the entire width of the rectangle as a percentage of the underlying frame width. For example, \\"80\\" means the rectangle width is 80% of the underlying frame width. The leftOffset and rectangleWidth must add up to 100% or less. This field corresponds to tts:extent - X in the TTML standard."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionRectangle) -> dict:
    out: dict = {}
    if "height" in value:
        out["height"] = value["height"]
    if "left_offset" in value:
        out["leftOffset"] = value["left_offset"]
    if "top_offset" in value:
        out["topOffset"] = value["top_offset"]
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> CaptionRectangle:
    out: CaptionRectangle = {}  # type: ignore[typeddict-item]
    if "height" in data:
        out["height"] = data["height"]
    if "leftOffset" in data:
        out["left_offset"] = data["leftOffset"]
    if "topOffset" in data:
        out["top_offset"] = data["topOffset"]
    if "width" in data:
        out["width"] = data["width"]
    return out
