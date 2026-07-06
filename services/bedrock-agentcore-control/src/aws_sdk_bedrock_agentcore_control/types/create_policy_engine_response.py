"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePolicyEngineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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


class CreatePolicyEngineResponse(TypedDict, closed=True):
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier for the created policy engine. This system-generated identifier consists of the user name plus a 10-character generated suffix and is used for all subsequent policy engine operations.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.policy_engine_name.PolicyEngineName"
    """<p>The customer-assigned name of the created policy engine. This matches the name provided in the request and serves as the human-readable identifier.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was created. This is automatically set by the service and used for auditing and lifecycle management.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was last updated. For newly created policy engines, this matches the <code>createdAt</code> timestamp.</p>"""
    policy_engine_arn: (
        "aws_sdk_bedrock_agentcore_control.types.policy_engine_arn.PolicyEngineArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created policy engine. This globally unique identifier can be used for cross-service references and IAM policy statements.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.policy_engine_status.PolicyEngineStatus"
    """<p>The current status of the policy engine. A status of <code>ACTIVE</code> indicates the policy engine is ready for use.</p>"""
    encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>A human-readable description of the policy engine's purpose.</p>"""
    status_reasons: "aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    """<p>Additional information about the policy engine status. This provides details about any failures or the current state of the policy engine creation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyEngineResponse) -> dict:
    out: dict = {}
    out["policyEngineId"] = value["policy_engine_id"]
    out["name"] = value["name"]
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
    out["policyEngineArn"] = value["policy_engine_arn"]
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_engine_status.serialize_json(
            value["status"]
        )
    )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.policy_status_reasons

    out["statusReasons"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.serialize_json(
            value["status_reasons"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePolicyEngineResponse:
    out: CreatePolicyEngineResponse = {}  # type: ignore[typeddict-item]
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError(
            "CreatePolicyEngineResponse.policy_engine_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePolicyEngineResponse.name required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyEngineResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyEngineResponse.updated_at required")
    if "policyEngineArn" in data:
        out["policy_engine_arn"] = data["policyEngineArn"]
    else:
        raise DeserializationError(
            "CreatePolicyEngineResponse.policy_engine_arn required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_engine_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_engine_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyEngineResponse.status required")
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "statusReasons" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_status_reasons

        out["status_reasons"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyEngineResponse.status_reasons required")
    return out
