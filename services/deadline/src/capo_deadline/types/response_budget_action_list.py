"""Generated from Smithy shape ``com.amazonaws.deadline#ResponseBudgetActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.response_budget_action

ResponseBudgetActionList: TypeAlias = list[
    "capo_deadline.types.response_budget_action.ResponseBudgetAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseBudgetActionList) -> list:
    import capo_deadline.types.response_budget_action

    out: list = []
    for item in value:
        out.append(capo_deadline.types.response_budget_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseBudgetActionList:
    import capo_deadline.types.response_budget_action

    out: ResponseBudgetActionList = []
    for item in data:
        out.append(capo_deadline.types.response_budget_action.deserialize_json(item))
    return out
