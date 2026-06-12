"""Generated from Smithy shape ``com.amazonaws.costexplorer#UtilizationsByTime``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.utilization_by_time

UtilizationsByTime: TypeAlias = list[
    "aws_sdk_cost_explorer.types.utilization_by_time.UtilizationByTime"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UtilizationsByTime) -> list:
    import aws_sdk_cost_explorer.types.utilization_by_time

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.utilization_by_time.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UtilizationsByTime:
    import aws_sdk_cost_explorer.types.utilization_by_time

    out: UtilizationsByTime = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.utilization_by_time.deserialize_aws_json_1_1(
                item
            )
        )
    return out
