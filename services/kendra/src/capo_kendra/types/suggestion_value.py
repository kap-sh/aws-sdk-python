"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.suggestion_text_with_highlights


class SuggestionValue(TypedDict, closed=True):
    text: NotRequired[
        "capo_kendra.types.suggestion_text_with_highlights.SuggestionTextWithHighlights"
    ]
    """<p>The <code>SuggestionTextWithHighlights</code> structure that contains the query suggestion text and highlights.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionValue) -> dict:
    out: dict = {}
    if "text" in value:
        import capo_kendra.types.suggestion_text_with_highlights

        out["Text"] = (
            capo_kendra.types.suggestion_text_with_highlights.serialize_aws_json_1_1(
                value["text"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuggestionValue:
    out: SuggestionValue = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        import capo_kendra.types.suggestion_text_with_highlights

        out["text"] = (
            capo_kendra.types.suggestion_text_with_highlights.deserialize_aws_json_1_1(
                data["Text"]
            )
        )
    return out
