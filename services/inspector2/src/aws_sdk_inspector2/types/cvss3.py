"""Generated from Smithy shape ``com.amazonaws.inspector2#Cvss3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cvss_base_score
    import aws_sdk_inspector2.types.cvss_scoring_vector


class Cvss3(TypedDict, closed=True):
    base_score: "aws_sdk_inspector2.types.cvss_base_score.CvssBaseScore"
    """<p>The CVSS v3 base score for the vulnerability.</p>"""
    scoring_vector: NotRequired[
        "aws_sdk_inspector2.types.cvss_scoring_vector.CvssScoringVector"
    ]
    """<p>The scoring vector associated with the CVSS v3 score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cvss3) -> dict:
    out: dict = {}
    out["baseScore"] = value.get("base_score", 0)
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    return out


def deserialize_json(data: dict) -> Cvss3:
    out: Cvss3 = {}  # type: ignore[typeddict-item]
    if "baseScore" in data:
        out["base_score"] = data["baseScore"]
    else:
        out["base_score"] = 0
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    return out
