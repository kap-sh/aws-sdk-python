"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeletePolicyEngineResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_arn
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_name
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_status
    import aws_sdk_bedrock_agentcore_control.types.policy_status_reasons
    import aws_sdk_bedrock_agentcore_control.types.resource_id

class DeletePolicyEngineResponse(TypedDict):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy engine being deleted. This confirms which policy engine the deletion operation targets.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.policy_engine_name.PolicyEngineName"
    """<p>The customer-assigned name of the deleted policy engine.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the deleted policy engine was originally created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the deleted policy engine was last modified before deletion. This tracks the final state of the policy engine before it was removed from the system.</p>"""
    policy_engine_arn: "aws_sdk_bedrock_agentcore_control.types.policy_engine_arn.PolicyEngineArn"
    """<p>The Amazon Resource Name (ARN) of the deleted policy engine. This globally unique identifier confirms which policy engine resource was successfully removed.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.policy_engine_status.PolicyEngineStatus"
    """<p>The status of the policy engine deletion operation. This provides status about any issues that occurred during the deletion process.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore_control.types.description.Description"]
    """<p>The human-readable description of the deleted policy engine.</p>"""
    status_reasons: "aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    """<p>Additional information about the deletion status. This provides details about the deletion process or any issues that may have occurred.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyEngineResponse) -> dict:
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
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.policy_status_reasons
    out["statusReasons"] = aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.serialize_json(value["status_reasons"])
    return out


def deserialize_json(data: dict) -> DeletePolicyEngineResponse:
    out: DeletePolicyEngineResponse = {}  # type: ignore[typeddict-item]
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("DeletePolicyEngineResponse.policy_engine_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeletePolicyEngineResponse.name required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("DeletePolicyEngineResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["updated_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["updatedAt"])
    else:
        raise DeserializationError("DeletePolicyEngineResponse.updated_at required")
    if "policyEngineArn" in data:
        out["policy_engine_arn"] = data["policyEngineArn"]
    else:
        raise DeserializationError("DeletePolicyEngineResponse.policy_engine_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_engine_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.policy_engine_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeletePolicyEngineResponse.status required")
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "statusReasons" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_status_reasons
        out["status_reasons"] = aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.deserialize_json(data["statusReasons"])
    else:
        raise DeserializationError("DeletePolicyEngineResponse.status_reasons required")
    return out