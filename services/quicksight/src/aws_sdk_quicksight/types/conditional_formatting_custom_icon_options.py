"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingCustomIconOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.icon
    import aws_sdk_quicksight.types.unicode_icon


class ConditionalFormattingCustomIconOptions(TypedDict):
    icon: NotRequired["aws_sdk_quicksight.types.icon.Icon"]
    """<p>Determines the type of icon.</p>"""
    unicode_icon: NotRequired["aws_sdk_quicksight.types.unicode_icon.UnicodeIcon"]
    """<p>Determines the Unicode icon type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingCustomIconOptions) -> dict:
    out: dict = {}
    if "icon" in value:
        import aws_sdk_quicksight.types.icon

        out["Icon"] = aws_sdk_quicksight.types.icon.serialize_json(value["icon"])
    if "unicode_icon" in value:
        out["UnicodeIcon"] = value["unicode_icon"]
    return out


def deserialize_json(data: dict) -> ConditionalFormattingCustomIconOptions:
    out: ConditionalFormattingCustomIconOptions = {}  # type: ignore[typeddict-item]
    if "Icon" in data:
        import aws_sdk_quicksight.types.icon

        out["icon"] = aws_sdk_quicksight.types.icon.deserialize_json(data["Icon"])
    if "UnicodeIcon" in data:
        out["unicode_icon"] = data["UnicodeIcon"]
    return out
