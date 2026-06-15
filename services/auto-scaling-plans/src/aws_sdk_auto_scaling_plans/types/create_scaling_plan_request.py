"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#CreateScalingPlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.application_source
    import aws_sdk_auto_scaling_plans.types.scaling_instructions
    import aws_sdk_auto_scaling_plans.types.scaling_plan_name


class CreateScalingPlanRequest(TypedDict):
    scaling_plan_name: (
        "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    )
    """<p>The name of the scaling plan. Names cannot contain vertical bars, colons, or forward slashes.</p>"""
    application_source: (
        "aws_sdk_auto_scaling_plans.types.application_source.ApplicationSource"
    )
    r"""<p>A CloudFormation stack or set of tags. You can create one scaling plan per application source.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html\">ApplicationSource</a> in the <i>AWS Auto Scaling API Reference</i>.</p>"""
    scaling_instructions: (
        "aws_sdk_auto_scaling_plans.types.scaling_instructions.ScalingInstructions"
    )
    r"""<p>The scaling instructions.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html\">ScalingInstruction</a> in the <i>AWS Auto Scaling API Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScalingPlanRequest) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    import aws_sdk_auto_scaling_plans.types.application_source

    out["ApplicationSource"] = (
        aws_sdk_auto_scaling_plans.types.application_source.serialize_aws_json_1_1(
            value["application_source"]
        )
    )
    import aws_sdk_auto_scaling_plans.types.scaling_instructions

    out["ScalingInstructions"] = (
        aws_sdk_auto_scaling_plans.types.scaling_instructions.serialize_aws_json_1_1(
            value["scaling_instructions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScalingPlanRequest:
    out: CreateScalingPlanRequest = {}  # type: ignore[typeddict-item]
    if "ScalingPlanName" in data:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        raise DeserializationError(
            "CreateScalingPlanRequest.scaling_plan_name required"
        )
    if "ApplicationSource" in data:
        import aws_sdk_auto_scaling_plans.types.application_source

        out["application_source"] = (
            aws_sdk_auto_scaling_plans.types.application_source.deserialize_aws_json_1_1(
                data["ApplicationSource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScalingPlanRequest.application_source required"
        )
    if "ScalingInstructions" in data:
        import aws_sdk_auto_scaling_plans.types.scaling_instructions

        out["scaling_instructions"] = (
            aws_sdk_auto_scaling_plans.types.scaling_instructions.deserialize_aws_json_1_1(
                data["ScalingInstructions"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScalingPlanRequest.scaling_instructions required"
        )
    return out
