"""Generated from Smithy shape ``com.amazonaws.budgets#ActionHistories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.action_history

ActionHistories: TypeAlias = list["aws_sdk_budgets.types.action_history.ActionHistory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionHistories) -> list:
    import aws_sdk_budgets.types.action_history

    out: list = []
    for item in value:
        out.append(aws_sdk_budgets.types.action_history.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ActionHistories:
    import aws_sdk_budgets.types.action_history

    out: ActionHistories = []
    for item in data:
        out.append(aws_sdk_budgets.types.action_history.deserialize_aws_json_1_1(item))
    return out
