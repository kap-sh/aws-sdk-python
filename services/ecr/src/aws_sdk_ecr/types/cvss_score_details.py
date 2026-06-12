"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScoreDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.cvss_score_adjustment_list
    import aws_sdk_ecr.types.score
    import aws_sdk_ecr.types.scoring_vector
    import aws_sdk_ecr.types.source
    import aws_sdk_ecr.types.version


class CvssScoreDetails(TypedDict):
    adjustments: NotRequired[
        "aws_sdk_ecr.types.cvss_score_adjustment_list.CvssScoreAdjustmentList"
    ]
    """<p>An object that contains details about adjustment Amazon Inspector made to the CVSS score.</p>"""
    score: "aws_sdk_ecr.types.score.Score"
    """<p>The CVSS score.</p>"""
    score_source: NotRequired["aws_sdk_ecr.types.source.Source"]
    """<p>The source for the CVSS score.</p>"""
    scoring_vector: NotRequired["aws_sdk_ecr.types.scoring_vector.ScoringVector"]
    """<p>The vector for the CVSS score.</p>"""
    version: NotRequired["aws_sdk_ecr.types.version.Version"]
    """<p>The CVSS version used in scoring.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CvssScoreDetails) -> dict:
    out: dict = {}
    if "adjustments" in value:
        import aws_sdk_ecr.types.cvss_score_adjustment_list

        out["adjustments"] = (
            aws_sdk_ecr.types.cvss_score_adjustment_list.serialize_aws_json_1_1(
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
        import aws_sdk_ecr.types.cvss_score_adjustment_list

        out["adjustments"] = (
            aws_sdk_ecr.types.cvss_score_adjustment_list.deserialize_aws_json_1_1(
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
