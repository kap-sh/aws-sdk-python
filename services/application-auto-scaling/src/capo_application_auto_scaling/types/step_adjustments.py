"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#StepAdjustments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.step_adjustment

StepAdjustments: TypeAlias = list[
    "capo_application_auto_scaling.types.step_adjustment.StepAdjustment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepAdjustments) -> list:
    import capo_application_auto_scaling.types.step_adjustment

    out: list = []
    for item in value:
        out.append(
            capo_application_auto_scaling.types.step_adjustment.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StepAdjustments:
    import capo_application_auto_scaling.types.step_adjustment

    out: StepAdjustments = []
    for item in data:
        out.append(
            capo_application_auto_scaling.types.step_adjustment.deserialize_aws_json_1_1(
                item
            )
        )
    return out
