"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyEngineSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.policy_engine_arn
    import capo_bedrock_agentcore_control.types.policy_engine_name
    import capo_bedrock_agentcore_control.types.policy_engine_status
    import capo_bedrock_agentcore_control.types.resource_id


class GetPolicyEngineSummaryResponse(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy engine.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_engine_name.PolicyEngineName"
    """<p>The customer-assigned name of the policy engine.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was originally created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy engine was last modified.</p>"""
    policy_engine_arn: (
        "capo_bedrock_agentcore_control.types.policy_engine_arn.PolicyEngineArn"
    )
    """<p>The Amazon Resource Name (ARN) of the policy engine.</p>"""
    status: (
        "capo_bedrock_agentcore_control.types.policy_engine_status.PolicyEngineStatus"
    )
    """<p>The current status of the policy engine.</p>"""
    encryption_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyEngineSummaryResponse) -> dict:
    out: dict = {}
    out["policyEngineId"] = value["policy_engine_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    out["policyEngineArn"] = value["policy_engine_arn"]
    import capo_bedrock_agentcore_control.types.policy_engine_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.policy_engine_status.serialize_json(
            value["status"]
        )
    )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> GetPolicyEngineSummaryResponse:
    out: GetPolicyEngineSummaryResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyEngineId") is not None:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError(
            "GetPolicyEngineSummaryResponse.policy_engine_id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.name required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.updated_at required")
    if data.get("policyEngineArn") is not None:
        out["policy_engine_arn"] = data["policyEngineArn"]
    else:
        raise DeserializationError(
            "GetPolicyEngineSummaryResponse.policy_engine_arn required"
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.policy_engine_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_engine_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetPolicyEngineSummaryResponse.status required")
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
