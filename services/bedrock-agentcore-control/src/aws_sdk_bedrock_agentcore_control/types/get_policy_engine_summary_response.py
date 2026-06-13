"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyEngineSummaryResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_arn
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_name
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_status
    import aws_sdk_bedrock_agentcore_control.types.resource_id

class GetPolicyEngineSummaryResponse(TypedDict):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy engine.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.policy_engine_name.PolicyEngineName"
    """<p>The customer-assigned name of the policy engine.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was originally created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was last modified.</p>"""
    policy_engine_arn: "aws_sdk_bedrock_agentcore_control.types.policy_engine_arn.PolicyEngineArn"
    """<p>The Amazon Resource Name (ARN) of the policy engine.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.policy_engine_status.PolicyEngineStatus"
    """<p>The current status of the policy engine.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyEngineSummaryResponse) -> dict:
    out: dict = {}
    out["policyEngineId"] = value["policy_engine_id"]
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["updatedAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["updated_at"])
    out["policyEngineArn"] = value["policy_engine_arn"]
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.policy_engine_status.serialize_json(value["status"])
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> GetPolicyEngineSummaryResponse:
    out: GetPolicyEngineSummaryResponse = {}  # type: ignore[typeddict-item]
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.policy_engine_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.name required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["updated_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["updatedAt"])
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.updated_at required")
    if "policyEngineArn" in data:
        out["policy_engine_arn"] = data["policyEngineArn"]
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.policy_engine_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_engine_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.policy_engine_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.status required")
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out