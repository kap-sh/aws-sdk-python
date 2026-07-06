"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeletePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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


class DeletePolicyResponse(TypedDict, closed=True):
    policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy being deleted. This confirms which policy the deletion operation targets.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The customer-assigned name of the deleted policy. This confirms which policy was successfully removed from the system and matches the name that was originally assigned during policy creation.</p>"""
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine from which the policy was deleted. This confirms the policy engine context for the deletion operation.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the deleted policy was originally created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the deleted policy was last modified before deletion. This tracks the final state of the policy before it was removed from the system.</p>"""
    policy_arn: "aws_sdk_bedrock_agentcore_control.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the deleted policy. This globally unique identifier confirms which policy resource was successfully removed.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.policy_status.PolicyStatus"
    """<p>The status of the policy deletion operation. This provides information about any issues that occurred during the deletion process.</p>"""
    definition: (
        "aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    )
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The human-readable description of the deleted policy.</p>"""
    status_reasons: "aws_sdk_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    """<p>Additional information about the deletion status. This provides details about the deletion process or any issues that may have occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyResponse) -> dict:
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


def deserialize_json(data: dict) -> DeletePolicyResponse:
    out: DeletePolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("DeletePolicyResponse.policy_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeletePolicyResponse.name required")
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("DeletePolicyResponse.policy_engine_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DeletePolicyResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DeletePolicyResponse.updated_at required")
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("DeletePolicyResponse.policy_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeletePolicyResponse.status required")
    if "definition" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("DeletePolicyResponse.definition required")
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
        raise DeserializationError("DeletePolicyResponse.status_reasons required")
    return out
