"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.base_score
    import aws_sdk_ecr.types.scoring_vector
    import aws_sdk_ecr.types.source
    import aws_sdk_ecr.types.version


class CvssScore(TypedDict, closed=True):
    base_score: "aws_sdk_ecr.types.base_score.BaseScore"
    """<p>The base CVSS score used for the finding.</p>"""
    scoring_vector: NotRequired["aws_sdk_ecr.types.scoring_vector.ScoringVector"]
    """<p>The vector string of the CVSS score.</p>"""
    source: NotRequired["aws_sdk_ecr.types.source.Source"]
    """<p>The source of the CVSS score.</p>"""
    version: NotRequired["aws_sdk_ecr.types.version.Version"]
    """<p>The version of CVSS used for the score.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CvssScore) -> dict:
    out: dict = {}
    out["baseScore"] = value.get("base_score", 0)
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    if "source" in value:
        out["source"] = value["source"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CvssScore:
    out: CvssScore = {}  # type: ignore[typeddict-item]
    if "baseScore" in data:
        out["base_score"] = data["baseScore"]
    else:
        out["base_score"] = 0
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    if "source" in data:
        out["source"] = data["source"]
    if "version" in data:
        out["version"] = data["version"]
    return out
