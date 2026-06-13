"""Generated from Smithy shape ``com.amazonaws.inspector2#Epss``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.epss_score


class Epss(TypedDict):
    score: "aws_sdk_inspector2.types.epss_score.EpssScore"
    """<p>The Exploit Prediction Scoring System (EPSS) score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Epss) -> dict:
    out: dict = {}
    out["score"] = value.get("score", 0)
    return out


def deserialize_json(data: dict) -> Epss:
    out: Epss = {}  # type: ignore[typeddict-item]
    if "score" in data:
        out["score"] = data["score"]
    else:
        out["score"] = 0
    return out
