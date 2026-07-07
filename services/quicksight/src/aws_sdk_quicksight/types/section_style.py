"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.spacing


class SectionStyle(TypedDict, closed=True):
    height: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>The height of a section.</p> <p>Heights can only be defined for header and footer sections. The default height margin is 0.5 inches. </p>"""
    padding: NotRequired["aws_sdk_quicksight.types.spacing.Spacing"]
    """<p>The spacing between section content and its top, bottom, left, and right edges.</p> <p>There is no padding by default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionStyle) -> dict:
    out: dict = {}
    if "height" in value:
        out["Height"] = value["height"]
    if "padding" in value:
        import aws_sdk_quicksight.types.spacing

        out["Padding"] = aws_sdk_quicksight.types.spacing.serialize_json(
            value["padding"]
        )
    return out


def deserialize_json(data: dict) -> SectionStyle:
    out: SectionStyle = {}  # type: ignore[typeddict-item]
    if "Height" in data:
        out["height"] = data["Height"]
    if "Padding" in data:
        import aws_sdk_quicksight.types.spacing

        out["padding"] = aws_sdk_quicksight.types.spacing.deserialize_json(
            data["Padding"]
        )
    return out
