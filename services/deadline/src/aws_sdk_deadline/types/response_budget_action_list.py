"""Generated from Smithy shape ``com.amazonaws.deadline#ResponseBudgetActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.response_budget_action

ResponseBudgetActionList: TypeAlias = list[
    "aws_sdk_deadline.types.response_budget_action.ResponseBudgetAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseBudgetActionList) -> list:
    import aws_sdk_deadline.types.response_budget_action

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.response_budget_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseBudgetActionList:
    import aws_sdk_deadline.types.response_budget_action

    out: ResponseBudgetActionList = []
    for item in data:
        out.append(aws_sdk_deadline.types.response_budget_action.deserialize_json(item))
    return out
