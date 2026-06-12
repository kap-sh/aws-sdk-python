"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanExtensionOfferings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_plan_extension_offering

TrainingPlanExtensionOfferings: TypeAlias = list[
    "aws_sdk_sagemaker.types.training_plan_extension_offering.TrainingPlanExtensionOffering"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanExtensionOfferings) -> list:
    import aws_sdk_sagemaker.types.training_plan_extension_offering

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.training_plan_extension_offering.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingPlanExtensionOfferings:
    import aws_sdk_sagemaker.types.training_plan_extension_offering

    out: TrainingPlanExtensionOfferings = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.training_plan_extension_offering.deserialize_aws_json_1_1(
                item
            )
        )
    return out
