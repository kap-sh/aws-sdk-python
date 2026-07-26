"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string


class CvssScore(TypedDict, closed=True):
    base_score: "float"
    """<p>The base CVSS score used for the finding.</p>"""
    scoring_vector: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The vector string of the CVSS score.</p>"""
    version: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The version of CVSS used for the score.</p>"""
    source: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The source of the CVSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScore) -> dict:
    out: dict = {}
    out["baseScore"] = value["base_score"]
    out["scoringVector"] = value["scoring_vector"]
    out["version"] = value["version"]
    out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> CvssScore:
    out: CvssScore = {}  # type: ignore[typeddict-item]
    if "baseScore" in data:
        out["base_score"] = data["baseScore"]
    else:
        raise DeserializationError("CvssScore.base_score required")
    if "scoringVector" in data:
        out["scoring_vector"] = data["scoringVector"]
    else:
        raise DeserializationError("CvssScore.scoring_vector required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CvssScore.version required")
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("CvssScore.source required")
    return out
