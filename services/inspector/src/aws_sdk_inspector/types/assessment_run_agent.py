"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunAgent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_health
    import aws_sdk_inspector.types.agent_health_code
    import aws_sdk_inspector.types.agent_id
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.auto_scaling_group
    import aws_sdk_inspector.types.message
    import aws_sdk_inspector.types.telemetry_metadata_list


class AssessmentRunAgent(TypedDict, closed=True):
    agent_id: "aws_sdk_inspector.types.agent_id.AgentId"
    """<p>The AWS account of the EC2 instance where the agent is installed.</p>"""
    assessment_run_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that is associated with the agent.</p>"""
    agent_health: "aws_sdk_inspector.types.agent_health.AgentHealth"
    """<p>The current health state of the agent.</p>"""
    agent_health_code: "aws_sdk_inspector.types.agent_health_code.AgentHealthCode"
    """<p>The detailed health state of the agent.</p>"""
    agent_health_details: NotRequired["aws_sdk_inspector.types.message.Message"]
    """<p>The description for the agent health code.</p>"""
    auto_scaling_group: NotRequired[
        "aws_sdk_inspector.types.auto_scaling_group.AutoScalingGroup"
    ]
    """<p>The Auto Scaling group of the EC2 instance that is specified by the agent ID.</p>"""
    telemetry_metadata: (
        "aws_sdk_inspector.types.telemetry_metadata_list.TelemetryMetadataList"
    )
    """<p>The Amazon Inspector application data metrics that are collected by the agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunAgent) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["assessmentRunArn"] = value["assessment_run_arn"]
    import aws_sdk_inspector.types.agent_health

    out["agentHealth"] = aws_sdk_inspector.types.agent_health.serialize_aws_json_1_1(
        value["agent_health"]
    )
    import aws_sdk_inspector.types.agent_health_code

    out["agentHealthCode"] = (
        aws_sdk_inspector.types.agent_health_code.serialize_aws_json_1_1(
            value["agent_health_code"]
        )
    )
    if "agent_health_details" in value:
        out["agentHealthDetails"] = value["agent_health_details"]
    if "auto_scaling_group" in value:
        out["autoScalingGroup"] = value["auto_scaling_group"]
    import aws_sdk_inspector.types.telemetry_metadata_list

    out["telemetryMetadata"] = (
        aws_sdk_inspector.types.telemetry_metadata_list.serialize_aws_json_1_1(
            value["telemetry_metadata"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunAgent:
    out: AssessmentRunAgent = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AssessmentRunAgent.agent_id required")
    if "assessmentRunArn" in data:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        raise DeserializationError("AssessmentRunAgent.assessment_run_arn required")
    if "agentHealth" in data:
        import aws_sdk_inspector.types.agent_health

        out["agent_health"] = (
            aws_sdk_inspector.types.agent_health.deserialize_aws_json_1_1(
                data["agentHealth"]
            )
        )
    else:
        raise DeserializationError("AssessmentRunAgent.agent_health required")
    if "agentHealthCode" in data:
        import aws_sdk_inspector.types.agent_health_code

        out["agent_health_code"] = (
            aws_sdk_inspector.types.agent_health_code.deserialize_aws_json_1_1(
                data["agentHealthCode"]
            )
        )
    else:
        raise DeserializationError("AssessmentRunAgent.agent_health_code required")
    if "agentHealthDetails" in data:
        out["agent_health_details"] = data["agentHealthDetails"]
    if "autoScalingGroup" in data:
        out["auto_scaling_group"] = data["autoScalingGroup"]
    if "telemetryMetadata" in data:
        import aws_sdk_inspector.types.telemetry_metadata_list

        out["telemetry_metadata"] = (
            aws_sdk_inspector.types.telemetry_metadata_list.deserialize_aws_json_1_1(
                data["telemetryMetadata"]
            )
        )
    else:
        raise DeserializationError("AssessmentRunAgent.telemetry_metadata required")
    return out
