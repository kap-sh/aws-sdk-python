"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourcesBudgetEstimate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_budget_estimate

ResourcesBudgetEstimate: TypeAlias = list[
    "aws_sdk_lightsail.types.resource_budget_estimate.ResourceBudgetEstimate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcesBudgetEstimate) -> list:
    import aws_sdk_lightsail.types.resource_budget_estimate

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.resource_budget_estimate.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourcesBudgetEstimate:
    import aws_sdk_lightsail.types.resource_budget_estimate

    out: ResourcesBudgetEstimate = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.resource_budget_estimate.deserialize_aws_json_1_1(
                item
            )
        )
    return out
