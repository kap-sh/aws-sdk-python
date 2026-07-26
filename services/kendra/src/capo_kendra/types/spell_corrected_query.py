"""Generated from Smithy shape ``com.amazonaws.kendra#SpellCorrectedQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.correction_list
    import capo_kendra.types.suggested_query_text


class SpellCorrectedQuery(TypedDict, closed=True):
    suggested_query_text: NotRequired[
        "capo_kendra.types.suggested_query_text.SuggestedQueryText"
    ]
    """<p>The query with the suggested spell corrections.</p>"""
    corrections: NotRequired["capo_kendra.types.correction_list.CorrectionList"]
    """<p>The corrected misspelled word or words in a query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpellCorrectedQuery) -> dict:
    out: dict = {}
    if "suggested_query_text" in value:
        out["SuggestedQueryText"] = value["suggested_query_text"]
    if "corrections" in value:
        import capo_kendra.types.correction_list

        out["Corrections"] = capo_kendra.types.correction_list.serialize_aws_json_1_1(
            value["corrections"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpellCorrectedQuery:
    out: SpellCorrectedQuery = {}  # type: ignore[typeddict-item]
    if "SuggestedQueryText" in data:
        out["suggested_query_text"] = data["SuggestedQueryText"]
    if "Corrections" in data:
        import capo_kendra.types.correction_list

        out["corrections"] = capo_kendra.types.correction_list.deserialize_aws_json_1_1(
            data["Corrections"]
        )
    return out
