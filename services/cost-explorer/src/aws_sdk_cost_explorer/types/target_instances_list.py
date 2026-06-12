"""Generated from Smithy shape ``com.amazonaws.costexplorer#TargetInstancesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.target_instance

TargetInstancesList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.target_instance.TargetInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetInstancesList) -> list:
    import aws_sdk_cost_explorer.types.target_instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.target_instance.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetInstancesList:
    import aws_sdk_cost_explorer.types.target_instance

    out: TargetInstancesList = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.target_instance.deserialize_aws_json_1_1(item)
        )
    return out
