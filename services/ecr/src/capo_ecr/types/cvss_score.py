"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.base_score
    import capo_ecr.types.scoring_vector
    import capo_ecr.types.source
    import capo_ecr.types.version


class CvssScore(TypedDict, closed=True):
    base_score: "capo_ecr.types.base_score.BaseScore"
    """<p>The base CVSS score used for the finding.</p>"""
    scoring_vector: NotRequired["capo_ecr.types.scoring_vector.ScoringVector"]
    """<p>The vector string of the CVSS score.</p>"""
    source: NotRequired["capo_ecr.types.source.Source"]
    """<p>The source of the CVSS score.</p>"""
    version: NotRequired["capo_ecr.types.version.Version"]
    """<p>The version of CVSS used for the score.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CvssScore) -> dict:
    out: dict = {}
    out["baseScore"] = (
        "NaN"
        if value.get("base_score", 0) != value.get("base_score", 0)
        else "Infinity"
        if value.get("base_score", 0) == float("inf")
        else "-Infinity"
        if value.get("base_score", 0) == float("-inf")
        else value.get("base_score", 0)
    )
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    if "source" in value:
        out["source"] = value["source"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CvssScore:
    out: CvssScore = {}  # type: ignore[typeddict-item]
    if data.get("baseScore") is not None:
        out["base_score"] = float(data["baseScore"])
    else:
        out["base_score"] = 0
    if data.get("scoringVector") is not None:
        out["scoring_vector"] = data["scoringVector"]
    if data.get("source") is not None:
        out["source"] = data["source"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
