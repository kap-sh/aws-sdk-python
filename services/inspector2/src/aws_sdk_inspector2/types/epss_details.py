"""Generated from Smithy shape ``com.amazonaws.inspector2#EpssDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.epss_score_value


class EpssDetails(TypedDict, closed=True):
    score: "aws_sdk_inspector2.types.epss_score_value.EpssScoreValue"
    """<p>The EPSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EpssDetails) -> dict:
    out: dict = {}
    out["score"] = value.get("score", 0)
    return out


def deserialize_json(data: dict) -> EpssDetails:
    out: EpssDetails = {}  # type: ignore[typeddict-item]
    if "score" in data:
        out["score"] = data["score"]
    else:
        out["score"] = 0
    return out
