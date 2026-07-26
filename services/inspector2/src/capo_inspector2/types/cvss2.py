"""Generated from Smithy shape ``com.amazonaws.inspector2#Cvss2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cvss_base_score
    import capo_inspector2.types.cvss_scoring_vector


class Cvss2(TypedDict, closed=True):
    base_score: "capo_inspector2.types.cvss_base_score.CvssBaseScore"
    """<p>The CVSS v2 base score for the vulnerability.</p>"""
    scoring_vector: NotRequired[
        "capo_inspector2.types.cvss_scoring_vector.CvssScoringVector"
    ]
    """<p>The scoring vector associated with the CVSS v2 score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cvss2) -> dict:
    out: dict = {}
    out["baseScore"] = value.get("base_score", 0)
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    return out


def deserialize_json(data: dict) -> Cvss2:
    out: Cvss2 = {}  # type: ignore[typeddict-item]
    if "baseScore" in data:
        out["base_score"] = data["baseScore"]
    else:
        out["base_score"] = 0
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    return out
