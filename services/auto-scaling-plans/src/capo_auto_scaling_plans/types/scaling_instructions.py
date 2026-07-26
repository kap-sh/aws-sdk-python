"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingInstructions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.scaling_instruction

ScalingInstructions: TypeAlias = list[
    "capo_auto_scaling_plans.types.scaling_instruction.ScalingInstruction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingInstructions) -> list:
    import capo_auto_scaling_plans.types.scaling_instruction

    out: list = []
    for item in value:
        out.append(
            capo_auto_scaling_plans.types.scaling_instruction.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingInstructions:
    import capo_auto_scaling_plans.types.scaling_instruction

    out: ScalingInstructions = []
    for item in data:
        out.append(
            capo_auto_scaling_plans.types.scaling_instruction.deserialize_aws_json_1_1(
                item
            )
        )
    return out
