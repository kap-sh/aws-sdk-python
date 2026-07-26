"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CvssScoreAdjustment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_string


class CvssScoreAdjustment(TypedDict, closed=True):
    metric: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The metric that Amazon Inspector used to adjust the CVSS score.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the CVSS score adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreAdjustment) -> dict:
    out: dict = {}
    if "metric" in value:
        out["metric"] = value["metric"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CvssScoreAdjustment:
    out: CvssScoreAdjustment = {}  # type: ignore[typeddict-item]
    if "metric" in data:
        out["metric"] = data["metric"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
