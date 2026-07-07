"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScoreDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cvss_score_adjustment_list
    import aws_sdk_inspector2.types.non_empty_string


class CvssScoreDetails(TypedDict, closed=True):
    score_source: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The source for the CVSS score.</p>"""
    cvss_source: NotRequired["aws_sdk_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The source of the CVSS data.</p>"""
    version: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The CVSS version used in scoring.</p>"""
    score: "float"
    """<p>The CVSS score.</p>"""
    scoring_vector: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The vector for the CVSS score.</p>"""
    adjustments: NotRequired[
        "aws_sdk_inspector2.types.cvss_score_adjustment_list.CvssScoreAdjustmentList"
    ]
    """<p>An object that contains details about adjustment Amazon Inspector made to the CVSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreDetails) -> dict:
    out: dict = {}
    out["scoreSource"] = value["score_source"]
    if "cvss_source" in value:
        out["cvssSource"] = value["cvss_source"]
    out["version"] = value["version"]
    out["score"] = value["score"]
    out["scoringVector"] = value["scoring_vector"]
    if "adjustments" in value:
        import aws_sdk_inspector2.types.cvss_score_adjustment_list

        out["adjustments"] = (
            aws_sdk_inspector2.types.cvss_score_adjustment_list.serialize_json(
                value["adjustments"]
            )
        )
    return out


def deserialize_json(data: dict) -> CvssScoreDetails:
    out: CvssScoreDetails = {}  # type: ignore[typeddict-item]
    if "scoreSource" in data:
        out["score_source"] = data["scoreSource"]
    else:
        raise DeserializationError("CvssScoreDetails.score_source required")
    if "cvssSource" in data:
        out["cvss_source"] = data["cvssSource"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CvssScoreDetails.version required")
    if "score" in data:
        out["score"] = data["score"]
    else:
        raise DeserializationError("CvssScoreDetails.score required")
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    else:
        raise DeserializationError("CvssScoreDetails.scoring_vector required")
    if "adjustments" in data:
        import aws_sdk_inspector2.types.cvss_score_adjustment_list

        out["adjustments"] = (
            aws_sdk_inspector2.types.cvss_score_adjustment_list.deserialize_json(
                data["adjustments"]
            )
        )
    return out
