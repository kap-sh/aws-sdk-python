"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanOfferings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_plan_offering

TrainingPlanOfferings: TypeAlias = list[
    "aws_sdk_sagemaker.types.training_plan_offering.TrainingPlanOffering"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanOfferings) -> list:
    import aws_sdk_sagemaker.types.training_plan_offering

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.training_plan_offering.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingPlanOfferings:
    import aws_sdk_sagemaker.types.training_plan_offering

    out: TrainingPlanOfferings = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.training_plan_offering.deserialize_aws_json_1_1(
                item
            )
        )
    return out
