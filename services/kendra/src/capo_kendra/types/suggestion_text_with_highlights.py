"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionTextWithHighlights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.string
    import capo_kendra.types.suggestion_highlight_list


class SuggestionTextWithHighlights(TypedDict, closed=True):
    text: NotRequired["capo_kendra.types.string.String"]
    """<p>The query suggestion text to display to the user.</p>"""
    highlights: NotRequired[
        "capo_kendra.types.suggestion_highlight_list.SuggestionHighlightList"
    ]
    """<p>The beginning and end of the query suggestion text that should be highlighted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionTextWithHighlights) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "highlights" in value:
        import capo_kendra.types.suggestion_highlight_list

        out["Highlights"] = (
            capo_kendra.types.suggestion_highlight_list.serialize_aws_json_1_1(
                value["highlights"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuggestionTextWithHighlights:
    out: SuggestionTextWithHighlights = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Highlights" in data:
        import capo_kendra.types.suggestion_highlight_list

        out["highlights"] = (
            capo_kendra.types.suggestion_highlight_list.deserialize_aws_json_1_1(
                data["Highlights"]
            )
        )
    return out
