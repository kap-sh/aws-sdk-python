"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceImprovementPlans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_improvement_plan

ChoiceImprovementPlans: TypeAlias = list[
    "capo_wellarchitected.types.choice_improvement_plan.ChoiceImprovementPlan"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceImprovementPlans) -> list:
    import capo_wellarchitected.types.choice_improvement_plan

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.choice_improvement_plan.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChoiceImprovementPlans:
    import capo_wellarchitected.types.choice_improvement_plan

    out: ChoiceImprovementPlans = []
    for item in data:
        out.append(
            capo_wellarchitected.types.choice_improvement_plan.deserialize_json(item)
        )
    return out
