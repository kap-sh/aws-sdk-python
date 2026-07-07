"""Generated from Smithy shape ``com.amazonaws.kendra#TextWithHighlights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.highlight_list
    import aws_sdk_kendra.types.string


class TextWithHighlights(TypedDict, closed=True):
    text: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>The text to display to the user.</p>"""
    highlights: NotRequired["aws_sdk_kendra.types.highlight_list.HighlightList"]
    """<p>The beginning and end of the text that should be highlighted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextWithHighlights) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "highlights" in value:
        import aws_sdk_kendra.types.highlight_list

        out["Highlights"] = aws_sdk_kendra.types.highlight_list.serialize_aws_json_1_1(
            value["highlights"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextWithHighlights:
    out: TextWithHighlights = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Highlights" in data:
        import aws_sdk_kendra.types.highlight_list

        out["highlights"] = (
            aws_sdk_kendra.types.highlight_list.deserialize_aws_json_1_1(
                data["Highlights"]
            )
        )
    return out
