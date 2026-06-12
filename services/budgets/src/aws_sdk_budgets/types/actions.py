"""Generated from Smithy shape ``com.amazonaws.budgets#Actions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.action

Actions: TypeAlias = list["aws_sdk_budgets.types.action.Action"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Actions) -> list:
    import aws_sdk_budgets.types.action

    out: list = []
    for item in value:
        out.append(aws_sdk_budgets.types.action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Actions:
    import aws_sdk_budgets.types.action

    out: Actions = []
    for item in data:
        out.append(aws_sdk_budgets.types.action.deserialize_aws_json_1_1(item))
    return out
