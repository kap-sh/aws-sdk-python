"""Generated from Smithy shape ``com.amazonaws.budgets#TargetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.target_id

TargetIds: TypeAlias = list["capo_budgets.types.target_id.TargetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetIds:
    return list(data)
