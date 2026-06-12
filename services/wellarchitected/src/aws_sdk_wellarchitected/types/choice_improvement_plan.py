"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceImprovementPlan``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice_id
    import aws_sdk_wellarchitected.types.display_text
    import aws_sdk_wellarchitected.types.improvement_plan_url


class ChoiceImprovementPlan(TypedDict):
    choice_id: NotRequired["aws_sdk_wellarchitected.types.choice_id.ChoiceId"]
    display_text: NotRequired["aws_sdk_wellarchitected.types.display_text.DisplayText"]
    """<p>The display text for the improvement plan.</p>"""
    improvement_plan_url: NotRequired[
        "aws_sdk_wellarchitected.types.improvement_plan_url.ImprovementPlanUrl"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceImprovementPlan) -> dict:
    out: dict = {}
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "display_text" in value:
        out["DisplayText"] = value["display_text"]
    if "improvement_plan_url" in value:
        out["ImprovementPlanUrl"] = value["improvement_plan_url"]
    return out


def deserialize_json(data: dict) -> ChoiceImprovementPlan:
    out: ChoiceImprovementPlan = {}  # type: ignore[typeddict-item]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    if "DisplayText" in data:
        out["display_text"] = data["DisplayText"]
    if "ImprovementPlanUrl" in data:
        out["improvement_plan_url"] = data["ImprovementPlanUrl"]
    return out
