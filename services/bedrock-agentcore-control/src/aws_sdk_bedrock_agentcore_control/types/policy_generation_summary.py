"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_arn
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_name
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_status
    import aws_sdk_bedrock_agentcore_control.types.resource
    import aws_sdk_bedrock_agentcore_control.types.resource_id
    import aws_sdk_bedrock_agentcore_control.types.string


class PolicyGenerationSummary(TypedDict):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine associated with this generation request.</p>"""
    policy_generation_id: (
        "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    )
    """<p>The unique identifier for this policy generation request.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.policy_generation_name.PolicyGenerationName"
    """<p>The customer-assigned name for this policy generation request.</p>"""
    policy_generation_arn: "aws_sdk_bedrock_agentcore_control.types.policy_generation_arn.PolicyGenerationArn"
    """<p>The ARN of this policy generation request.</p>"""
    resource: "aws_sdk_bedrock_agentcore_control.types.resource.Resource"
    """<p>The resource information associated with this policy generation.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this policy generation request was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this policy generation was last updated.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.policy_generation_status.PolicyGenerationStatus"
    """<p>The current status of this policy generation request.</p>"""
    findings: NotRequired["aws_sdk_bedrock_agentcore_control.types.string.String"]
    """<p>Findings and insights from this policy generation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationSummary) -> dict:
    out: dict = {}
    out["policyEngineId"] = value["policy_engine_id"]
    out["policyGenerationId"] = value["policy_generation_id"]
    out["name"] = value["name"]
    out["policyGenerationArn"] = value["policy_generation_arn"]
    import aws_sdk_bedrock_agentcore_control.types.resource

    out["resource"] = aws_sdk_bedrock_agentcore_control.types.resource.serialize_json(
        value["resource"]
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_generation_status.serialize_json(
            value["status"]
        )
    )
    if "findings" in value:
        out["findings"] = value["findings"]
    return out


def deserialize_json(data: dict) -> PolicyGenerationSummary:
    out: PolicyGenerationSummary = {}  # type: ignore[typeddict-item]
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("PolicyGenerationSummary.policy_engine_id required")
    if "policyGenerationId" in data:
        out["policy_generation_id"] = data["policyGenerationId"]
    else:
        raise DeserializationError(
            "PolicyGenerationSummary.policy_generation_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PolicyGenerationSummary.name required")
    if "policyGenerationArn" in data:
        out["policy_generation_arn"] = data["policyGenerationArn"]
    else:
        raise DeserializationError(
            "PolicyGenerationSummary.policy_generation_arn required"
        )
    if "resource" in data:
        import aws_sdk_bedrock_agentcore_control.types.resource

        out["resource"] = (
            aws_sdk_bedrock_agentcore_control.types.resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("PolicyGenerationSummary.resource required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("PolicyGenerationSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("PolicyGenerationSummary.updated_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_generation_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_generation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("PolicyGenerationSummary.status required")
    if "findings" in data:
        out["findings"] = data["findings"]
    return out
