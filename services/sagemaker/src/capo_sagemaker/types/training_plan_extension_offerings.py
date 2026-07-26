"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanExtensionOfferings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_extension_offering

TrainingPlanExtensionOfferings: TypeAlias = list[
    "capo_sagemaker.types.training_plan_extension_offering.TrainingPlanExtensionOffering"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanExtensionOfferings) -> list:
    import capo_sagemaker.types.training_plan_extension_offering

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_plan_extension_offering.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingPlanExtensionOfferings:
    import capo_sagemaker.types.training_plan_extension_offering

    out: TrainingPlanExtensionOfferings = []
    for item in data:
        out.append(
            capo_sagemaker.types.training_plan_extension_offering.deserialize_aws_json_1_1(
                item
            )
        )
    return out
