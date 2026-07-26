"""Generated from Smithy shape ``com.amazonaws.kendra#AdditionalResultAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.text_with_highlights


class AdditionalResultAttributeValue(TypedDict, closed=True):
    text_with_highlights_value: NotRequired[
        "capo_kendra.types.text_with_highlights.TextWithHighlights"
    ]
    """<p>The text associated with the attribute and information about the highlight to apply to the text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalResultAttributeValue) -> dict:
    out: dict = {}
    if "text_with_highlights_value" in value:
        import capo_kendra.types.text_with_highlights

        out["TextWithHighlightsValue"] = (
            capo_kendra.types.text_with_highlights.serialize_aws_json_1_1(
                value["text_with_highlights_value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalResultAttributeValue:
    out: AdditionalResultAttributeValue = {}  # type: ignore[typeddict-item]
    if "TextWithHighlightsValue" in data:
        import capo_kendra.types.text_with_highlights

        out["text_with_highlights_value"] = (
            capo_kendra.types.text_with_highlights.deserialize_aws_json_1_1(
                data["TextWithHighlightsValue"]
            )
        )
    return out
