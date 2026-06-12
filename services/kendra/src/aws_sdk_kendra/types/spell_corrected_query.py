"""Generated from Smithy shape ``com.amazonaws.kendra#SpellCorrectedQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.correction_list
    import aws_sdk_kendra.types.suggested_query_text


class SpellCorrectedQuery(TypedDict):
    suggested_query_text: NotRequired[
        "aws_sdk_kendra.types.suggested_query_text.SuggestedQueryText"
    ]
    """<p>The query with the suggested spell corrections.</p>"""
    corrections: NotRequired["aws_sdk_kendra.types.correction_list.CorrectionList"]
    """<p>The corrected misspelled word or words in a query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpellCorrectedQuery) -> dict:
    out: dict = {}
    if "suggested_query_text" in value:
        out["SuggestedQueryText"] = value["suggested_query_text"]
    if "corrections" in value:
        import aws_sdk_kendra.types.correction_list

        out["Corrections"] = (
            aws_sdk_kendra.types.correction_list.serialize_aws_json_1_1(
                value["corrections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpellCorrectedQuery:
    out: SpellCorrectedQuery = {}  # type: ignore[typeddict-item]
    if "SuggestedQueryText" in data:
        out["suggested_query_text"] = data["SuggestedQueryText"]
    if "Corrections" in data:
        import aws_sdk_kendra.types.correction_list

        out["corrections"] = (
            aws_sdk_kendra.types.correction_list.deserialize_aws_json_1_1(
                data["Corrections"]
            )
        )
    return out
