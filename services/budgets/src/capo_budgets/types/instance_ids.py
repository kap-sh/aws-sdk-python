"""Generated from Smithy shape ``com.amazonaws.budgets#InstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.instance_id

InstanceIds: TypeAlias = list["capo_budgets.types.instance_id.InstanceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceIds:
    return list(data)
