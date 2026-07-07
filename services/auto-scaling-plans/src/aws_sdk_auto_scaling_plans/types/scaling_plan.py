"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.application_source
    import aws_sdk_auto_scaling_plans.types.scaling_instructions
    import aws_sdk_auto_scaling_plans.types.scaling_plan_name
    import aws_sdk_auto_scaling_plans.types.scaling_plan_status_code
    import aws_sdk_auto_scaling_plans.types.scaling_plan_version
    import aws_sdk_auto_scaling_plans.types.timestamp_type
    import aws_sdk_auto_scaling_plans.types.xml_string


class ScalingPlan(TypedDict, closed=True):
    scaling_plan_name: (
        "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    )
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan.</p>"""
    application_source: (
        "aws_sdk_auto_scaling_plans.types.application_source.ApplicationSource"
    )
    """<p>A CloudFormation stack or a set of tags. You can create one scaling plan per application source.</p>"""
    scaling_instructions: (
        "aws_sdk_auto_scaling_plans.types.scaling_instructions.ScalingInstructions"
    )
    """<p>The scaling instructions.</p>"""
    status_code: "aws_sdk_auto_scaling_plans.types.scaling_plan_status_code.ScalingPlanStatusCode"
    """<p>The status of the scaling plan.</p> <ul> <li> <p> <code>Active</code> - The scaling plan is active.</p> </li> <li> <p> <code>ActiveWithProblems</code> - The scaling plan is active, but the scaling configuration for one or more resources could not be applied.</p> </li> <li> <p> <code>CreationInProgress</code> - The scaling plan is being created.</p> </li> <li> <p> <code>CreationFailed</code> - The scaling plan could not be created.</p> </li> <li> <p> <code>DeletionInProgress</code> - The scaling plan is being deleted.</p> </li> <li> <p> <code>DeletionFailed</code> - The scaling plan could not be deleted.</p> </li> <li> <p> <code>UpdateInProgress</code> - The scaling plan is being updated.</p> </li> <li> <p> <code>UpdateFailed</code> - The scaling plan could not be updated.</p> </li> </ul>"""
    status_message: NotRequired["aws_sdk_auto_scaling_plans.types.xml_string.XmlString"]
    """<p>A simple message about the current status of the scaling plan.</p>"""
    status_start_time: NotRequired[
        "aws_sdk_auto_scaling_plans.types.timestamp_type.TimestampType"
    ]
    """<p>The Unix time stamp when the scaling plan entered the current status.</p>"""
    creation_time: NotRequired[
        "aws_sdk_auto_scaling_plans.types.timestamp_type.TimestampType"
    ]
    """<p>The Unix time stamp when the scaling plan was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPlan) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
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
    import aws_sdk_auto_scaling_plans.types.scaling_plan_status_code

    out["StatusCode"] = (
        aws_sdk_auto_scaling_plans.types.scaling_plan_status_code.serialize_aws_json_1_1(
            value["status_code"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "status_start_time" in value:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["StatusStartTime"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
                value["status_start_time"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["CreationTime"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPlan:
    out: ScalingPlan = {}  # type: ignore[typeddict-item]
    if "ScalingPlanName" in data:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        raise DeserializationError("ScalingPlan.scaling_plan_name required")
    if "ScalingPlanVersion" in data:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        raise DeserializationError("ScalingPlan.scaling_plan_version required")
    if "ApplicationSource" in data:
        import aws_sdk_auto_scaling_plans.types.application_source

        out["application_source"] = (
            aws_sdk_auto_scaling_plans.types.application_source.deserialize_aws_json_1_1(
                data["ApplicationSource"]
            )
        )
    else:
        raise DeserializationError("ScalingPlan.application_source required")
    if "ScalingInstructions" in data:
        import aws_sdk_auto_scaling_plans.types.scaling_instructions

        out["scaling_instructions"] = (
            aws_sdk_auto_scaling_plans.types.scaling_instructions.deserialize_aws_json_1_1(
                data["ScalingInstructions"]
            )
        )
    else:
        raise DeserializationError("ScalingPlan.scaling_instructions required")
    if "StatusCode" in data:
        import aws_sdk_auto_scaling_plans.types.scaling_plan_status_code

        out["status_code"] = (
            aws_sdk_auto_scaling_plans.types.scaling_plan_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    else:
        raise DeserializationError("ScalingPlan.status_code required")
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "StatusStartTime" in data:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["status_start_time"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["StatusStartTime"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["creation_time"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
