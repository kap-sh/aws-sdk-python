"""Generated from Smithy shape ``com.amazonaws.costexplorer#MonitorArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn

MonitorArnList: TypeAlias = list["capo_cost_explorer.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MonitorArnList:
    return list(data)
