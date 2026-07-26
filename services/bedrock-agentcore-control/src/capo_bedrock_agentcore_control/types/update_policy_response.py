"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.policy_arn
    import capo_bedrock_agentcore_control.types.policy_definition
    import capo_bedrock_agentcore_control.types.policy_name
    import capo_bedrock_agentcore_control.types.policy_status
    import capo_bedrock_agentcore_control.types.policy_status_reasons
    import capo_bedrock_agentcore_control.types.resource_id


class UpdatePolicyResponse(TypedDict, closed=True):
    policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the updated policy.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The name of the updated policy.</p>"""
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine managing the updated policy.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The original creation timestamp of the policy.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy was last updated.</p>"""
    policy_arn: "capo_bedrock_agentcore_control.types.policy_arn.PolicyArn"
    """<p>The ARN of the updated policy.</p>"""
    status: "capo_bedrock_agentcore_control.types.policy_status.PolicyStatus"
    """<p>The current status of the updated policy.</p>"""
    definition: (
        "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    )
    """<p>The updated Cedar policy statement.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The updated description of the policy.</p>"""
    status_reasons: (
        "capo_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    )
    """<p>Additional information about the update status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyResponse) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    out["name"] = value["name"]
    out["policyEngineId"] = value["policy_engine_id"]
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
    out["policyArn"] = value["policy_arn"]
    import capo_bedrock_agentcore_control.types.policy_status

    out["status"] = capo_bedrock_agentcore_control.types.policy_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore_control.types.policy_definition

    out["definition"] = (
        capo_bedrock_agentcore_control.types.policy_definition.serialize_json(
            value["definition"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.policy_status_reasons

    out["statusReasons"] = (
        capo_bedrock_agentcore_control.types.policy_status_reasons.serialize_json(
            value["status_reasons"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePolicyResponse:
    out: UpdatePolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("UpdatePolicyResponse.policy_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdatePolicyResponse.name required")
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError("UpdatePolicyResponse.policy_engine_id required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.updated_at required")
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("UpdatePolicyResponse.policy_arn required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.policy_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.status required")
    if "definition" in data:
        import capo_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            capo_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.definition required")
    if "description" in data:
        out["description"] = data["description"]
    if "statusReasons" in data:
        import capo_bedrock_agentcore_control.types.policy_status_reasons

        out["status_reasons"] = (
            capo_bedrock_agentcore_control.types.policy_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.status_reasons required")
    return out
