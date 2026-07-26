"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScoreAdjustment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string


class CvssScoreAdjustment(TypedDict, closed=True):
    metric: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The metric used to adjust the CVSS score.</p>"""
    reason: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The reason the CVSS score has been adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreAdjustment) -> dict:
    out: dict = {}
    out["metric"] = value["metric"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CvssScoreAdjustment:
    out: CvssScoreAdjustment = {}  # type: ignore[typeddict-item]
    if "metric" in data:
        out["metric"] = data["metric"]
    else:
        raise DeserializationError("CvssScoreAdjustment.metric required")
    if "reason" in data:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("CvssScoreAdjustment.reason required")
    return out
