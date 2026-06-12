"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.suggestion_text_with_highlights


class SuggestionValue(TypedDict):
    text: NotRequired[
        "aws_sdk_kendra.types.suggestion_text_with_highlights.SuggestionTextWithHighlights"
    ]
    """<p>The <code>SuggestionTextWithHighlights</code> structure that contains the query suggestion text and highlights.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionValue) -> dict:
    out: dict = {}
    if "text" in value:
        import aws_sdk_kendra.types.suggestion_text_with_highlights

        out["Text"] = (
            aws_sdk_kendra.types.suggestion_text_with_highlights.serialize_aws_json_1_1(
                value["text"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuggestionValue:
    out: SuggestionValue = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        import aws_sdk_kendra.types.suggestion_text_with_highlights

        out["text"] = (
            aws_sdk_kendra.types.suggestion_text_with_highlights.deserialize_aws_json_1_1(
                data["Text"]
            )
        )
    return out
