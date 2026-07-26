"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScoreDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.cvss_score_adjustment_list
    import capo_ecr.types.score
    import capo_ecr.types.scoring_vector
    import capo_ecr.types.source
    import capo_ecr.types.version


class CvssScoreDetails(TypedDict, closed=True):
    adjustments: NotRequired[
        "capo_ecr.types.cvss_score_adjustment_list.CvssScoreAdjustmentList"
    ]
    """<p>An object that contains details about adjustment Amazon Inspector made to the CVSS score.</p>"""
    score: "capo_ecr.types.score.Score"
    """<p>The CVSS score.</p>"""
    score_source: NotRequired["capo_ecr.types.source.Source"]
    """<p>The source for the CVSS score.</p>"""
    scoring_vector: NotRequired["capo_ecr.types.scoring_vector.ScoringVector"]
    """<p>The vector for the CVSS score.</p>"""
    version: NotRequired["capo_ecr.types.version.Version"]
    """<p>The CVSS version used in scoring.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CvssScoreDetails) -> dict:
    out: dict = {}
    if "adjustments" in value:
        import capo_ecr.types.cvss_score_adjustment_list

        out["adjustments"] = (
            capo_ecr.types.cvss_score_adjustment_list.serialize_aws_json_1_1(
                value["adjustments"]
            )
        )
    out["score"] = value.get("score", 0)
    if "score_source" in value:
        out["scoreSource"] = value["score_source"]
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CvssScoreDetails:
    out: CvssScoreDetails = {}  # type: ignore[typeddict-item]
    if "adjustments" in data:
        import capo_ecr.types.cvss_score_adjustment_list

        out["adjustments"] = (
            capo_ecr.types.cvss_score_adjustment_list.deserialize_aws_json_1_1(
                data["adjustments"]
            )
        )
    if "score" in data:
        out["score"] = data["score"]
    else:
        out["score"] = 0
    if "scoreSource" in data:
        out["score_source"] = data["scoreSource"]
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    if "version" in data:
        out["version"] = data["version"]
    return out
