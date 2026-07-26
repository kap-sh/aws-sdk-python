"""Generated from Smithy shape ``com.amazonaws.inspector2#Cvss4``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cvss_base_score
    import capo_inspector2.types.cvss_scoring_vector


class Cvss4(TypedDict, closed=True):
    base_score: "capo_inspector2.types.cvss_base_score.CvssBaseScore"
    """<p>The base CVSS v4 score for the vulnerability finding, which rates the severity of the vulnerability on a scale from 0 to 10.</p>"""
    scoring_vector: NotRequired[
        "capo_inspector2.types.cvss_scoring_vector.CvssScoringVector"
    ]
    """<p>The CVSS v4 scoring vector, which contains the metrics and measurements that were used to calculate the base score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cvss4) -> dict:
    out: dict = {}
    out["baseScore"] = value.get("base_score", 0)
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    return out


def deserialize_json(data: dict) -> Cvss4:
    out: Cvss4 = {}  # type: ignore[typeddict-item]
    if "baseScore" in data:
        out["base_score"] = data["baseScore"]
    else:
        out["base_score"] = 0
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    return out
