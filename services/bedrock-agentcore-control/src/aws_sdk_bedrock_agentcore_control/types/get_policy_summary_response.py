"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicySummaryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.policy_arn
    import aws_sdk_bedrock_agentcore_control.types.policy_name
    import aws_sdk_bedrock_agentcore_control.types.policy_status
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class GetPolicySummaryResponse(TypedDict):
    policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The customer-assigned name of the policy.</p>"""
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that manages this policy.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was originally created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was last modified.</p>"""
    policy_arn: "aws_sdk_bedrock_agentcore_control.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.policy_status.PolicyStatus"
    """<p>The current status of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicySummaryResponse) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    out["name"] = value["name"]
    out["policyEngineId"] = value["policy_engine_id"]
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
    out["policyArn"] = value["policy_arn"]
    import aws_sdk_bedrock_agentcore_control.types.policy_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPolicySummaryResponse:
    out: GetPolicySummaryResponse = {}  # type: ignore[typeddict-item]
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("GetPolicySummaryResponse.policy_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPolicySummaryResponse.name required")
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("GetPolicySummaryResponse.policy_engine_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicySummaryResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicySummaryResponse.updated_at required")
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("GetPolicySummaryResponse.policy_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetPolicySummaryResponse.status required")
    return out
