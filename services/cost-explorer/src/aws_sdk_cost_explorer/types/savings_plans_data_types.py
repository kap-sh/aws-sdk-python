"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansDataTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.savings_plans_data_type

SavingsPlansDataTypes: TypeAlias = list[
    "aws_sdk_cost_explorer.types.savings_plans_data_type.SavingsPlansDataType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansDataTypes) -> list:
    import aws_sdk_cost_explorer.types.savings_plans_data_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.savings_plans_data_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SavingsPlansDataTypes:
    import aws_sdk_cost_explorer.types.savings_plans_data_type

    out: SavingsPlansDataTypes = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.savings_plans_data_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
