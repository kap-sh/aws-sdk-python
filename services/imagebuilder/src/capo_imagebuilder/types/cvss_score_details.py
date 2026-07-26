"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CvssScoreDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.cvss_score_adjustment_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.non_negative_double


class CvssScoreDetails(TypedDict, closed=True):
    score_source: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The source for the CVSS score.</p>"""
    cvss_source: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The source of the finding.</p>"""
    version: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The CVSS version that generated the score.</p>"""
    score: NotRequired["capo_imagebuilder.types.non_negative_double.NonNegativeDouble"]
    """<p>The CVSS score.</p>"""
    scoring_vector: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>A vector that measures the severity of the vulnerability.</p>"""
    adjustments: NotRequired[
        "capo_imagebuilder.types.cvss_score_adjustment_list.CvssScoreAdjustmentList"
    ]
    """<p>An object that contains details about an adjustment that Amazon Inspector made to the CVSS score for the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreDetails) -> dict:
    out: dict = {}
    if "score_source" in value:
        out["scoreSource"] = value["score_source"]
    if "cvss_source" in value:
        out["cvssSource"] = value["cvss_source"]
    if "version" in value:
        out["version"] = value["version"]
    if "score" in value:
        out["score"] = value["score"]
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    if "adjustments" in value:
        import capo_imagebuilder.types.cvss_score_adjustment_list

        out["adjustments"] = (
            capo_imagebuilder.types.cvss_score_adjustment_list.serialize_json(
                value["adjustments"]
            )
        )
    return out


def deserialize_json(data: dict) -> CvssScoreDetails:
    out: CvssScoreDetails = {}  # type: ignore[typeddict-item]
    if "scoreSource" in data:
        out["score_source"] = data["scoreSource"]
    if "cvssSource" in data:
        out["cvss_source"] = data["cvssSource"]
    if "version" in data:
        out["version"] = data["version"]
    if "score" in data:
        out["score"] = data["score"]
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    if "adjustments" in data:
        import capo_imagebuilder.types.cvss_score_adjustment_list

        out["adjustments"] = (
            capo_imagebuilder.types.cvss_score_adjustment_list.deserialize_json(
                data["adjustments"]
            )
        )
    return out
