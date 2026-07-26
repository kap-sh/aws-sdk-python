"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.double
    import capo_connect.types.evaluation_score_percentage


class EvaluationScore(TypedDict, closed=True):
    percentage: (
        "capo_connect.types.evaluation_score_percentage.EvaluationScorePercentage"
    )
    """<p>The score percentage for an item in a contact evaluation.</p>"""
    not_applicable: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the item as not applicable for scoring.</p>"""
    automatic_fail: "capo_connect.types.boolean.Boolean"
    """<p>The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag will be true.</p>"""
    applied_weight: NotRequired["capo_connect.types.double.Double"]
    """<p>Weight applied to this evaluation score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationScore) -> dict:
    out: dict = {}
    out["Percentage"] = value.get("percentage", 0)
    out["NotApplicable"] = value.get("not_applicable", False)
    out["AutomaticFail"] = value.get("automatic_fail", False)
    if "applied_weight" in value:
        out["AppliedWeight"] = value["applied_weight"]
    return out


def deserialize_json(data: dict) -> EvaluationScore:
    out: EvaluationScore = {}  # type: ignore[typeddict-item]
    if "Percentage" in data:
        out["percentage"] = data["Percentage"]
    else:
        out["percentage"] = 0
    if "NotApplicable" in data:
        out["not_applicable"] = data["NotApplicable"]
    else:
        out["not_applicable"] = False
    if "AutomaticFail" in data:
        out["automatic_fail"] = data["AutomaticFail"]
    else:
        out["automatic_fail"] = False
    if "AppliedWeight" in data:
        out["applied_weight"] = data["AppliedWeight"]
    return out
