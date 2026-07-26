"""Generated from Smithy shape ``com.amazonaws.kendra#Correction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.integer
    import capo_kendra.types.string


class Correction(TypedDict, closed=True):
    begin_offset: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The zero-based location in the response string or text where the corrected word starts.</p>"""
    end_offset: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The zero-based location in the response string or text where the corrected word ends.</p>"""
    term: NotRequired["capo_kendra.types.string.String"]
    """<p>The string or text of a misspelled word in a query.</p>"""
    corrected_term: NotRequired["capo_kendra.types.string.String"]
    """<p>The string or text of a corrected misspelled word in a query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Correction) -> dict:
    out: dict = {}
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "term" in value:
        out["Term"] = value["term"]
    if "corrected_term" in value:
        out["CorrectedTerm"] = value["corrected_term"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Correction:
    out: Correction = {}  # type: ignore[typeddict-item]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "Term" in data:
        out["term"] = data["Term"]
    if "CorrectedTerm" in data:
        out["corrected_term"] = data["CorrectedTerm"]
    return out
