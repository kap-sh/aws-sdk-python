"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.policy_arn
    import aws_sdk_bedrock_agentcore_control.types.policy_definition
    import aws_sdk_bedrock_agentcore_control.types.policy_name
    import aws_sdk_bedrock_agentcore_control.types.policy_status
    import aws_sdk_bedrock_agentcore_control.types.policy_status_reasons
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class CreatePolicyResponse(TypedDict):
    policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier for the created policy. This is a system-generated identifier consisting of the user name plus a 10-character generated suffix, used for all subsequent policy operations.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The customer-assigned name of the created policy. This matches the name provided in the request and serves as the human-readable identifier for the policy.</p>"""
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that manages this policy. This confirms the policy engine assignment and is used for policy evaluation routing.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was created. This is automatically set by the service and used for auditing and lifecycle management.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was last updated. For newly created policies, this matches the createdAt timestamp.</p>"""
    policy_arn: "aws_sdk_bedrock_agentcore_control.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the created policy. This globally unique identifier can be used for cross-service references and IAM policy statements.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.policy_status.PolicyStatus"
    """<p>The current status of the policy. A status of <code>ACTIVE</code> indicates the policy is ready for use.</p>"""
    definition: (
        "aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    )
    """<p>The Cedar policy statement that was created. This is the validated policy definition that will be used for agent behavior control and access decisions.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The human-readable description of the policy's purpose and functionality. This helps administrators understand and manage the policy.</p>"""
    status_reasons: "aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    """<p>Additional information about the policy status. This provides details about any failures or the current state of the policy creation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyResponse) -> dict:
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
    import aws_sdk_bedrock_agentcore_control.types.policy_definition

    out["definition"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_definition.serialize_json(
            value["definition"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.policy_status_reasons

    out["statusReasons"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.serialize_json(
            value["status_reasons"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePolicyResponse:
    out: CreatePolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("CreatePolicyResponse.policy_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePolicyResponse.name required")
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("CreatePolicyResponse.policy_engine_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyResponse.updated_at required")
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("CreatePolicyResponse.policy_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyResponse.status required")
    if "definition" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyResponse.definition required")
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
        raise DeserializationError("CreatePolicyResponse.status_reasons required")
    return out
