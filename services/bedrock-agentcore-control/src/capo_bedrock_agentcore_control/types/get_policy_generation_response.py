"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.policy_generation_arn
    import capo_bedrock_agentcore_control.types.policy_generation_name
    import capo_bedrock_agentcore_control.types.policy_generation_status
    import capo_bedrock_agentcore_control.types.policy_status_reasons
    import capo_bedrock_agentcore_control.types.resource
    import capo_bedrock_agentcore_control.types.resource_id
    import capo_bedrock_agentcore_control.types.string


class GetPolicyGenerationResponse(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine associated with this policy generation. This confirms the policy engine context for the generation operation.</p>"""
    policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy generation request. This matches the generation ID provided in the request and serves as the tracking identifier.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_generation_name.PolicyGenerationName"
    """<p>The customer-assigned name for the policy generation request. This helps identify and track generation operations across multiple requests.</p>"""
    policy_generation_arn: (
        "capo_bedrock_agentcore_control.types.policy_generation_arn.PolicyGenerationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the policy generation. This globally unique identifier can be used for tracking, auditing, and cross-service references.</p>"""
    resource: "capo_bedrock_agentcore_control.types.resource.Resource"
    """<p>The resource information associated with the policy generation. This provides context about the target resources for which the policies are being generated.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy generation request was created. This is used for tracking and auditing generation operations and their lifecycle.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the policy generation was last updated. This tracks the progress of the generation process and any status changes.</p>"""
    status: "capo_bedrock_agentcore_control.types.policy_generation_status.PolicyGenerationStatus"
    """<p>The current status of the policy generation. This indicates whether the generation is in progress, completed successfully, or failed during processing.</p>"""
    findings: NotRequired["capo_bedrock_agentcore_control.types.string.String"]
    """<p>The findings and results from the policy generation process. This includes any issues, recommendations, validation results, or insights from the generated policies.</p>"""
    status_reasons: (
        "capo_bedrock_agentcore_control.types.policy_status_reasons.PolicyStatusReasons"
    )
    """<p>Additional information about the generation status. This provides details about any failures, warnings, or the current state of the generation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyGenerationResponse) -> dict:
    out: dict = {}
    out["policyEngineId"] = value["policy_engine_id"]
    out["policyGenerationId"] = value["policy_generation_id"]
    out["name"] = value["name"]
    out["policyGenerationArn"] = value["policy_generation_arn"]
    import capo_bedrock_agentcore_control.types.resource

    out["resource"] = capo_bedrock_agentcore_control.types.resource.serialize_json(
        value["resource"]
    )
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
    import capo_bedrock_agentcore_control.types.policy_generation_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.policy_generation_status.serialize_json(
            value["status"]
        )
    )
    if "findings" in value:
        out["findings"] = value["findings"]
    import capo_bedrock_agentcore_control.types.policy_status_reasons

    out["statusReasons"] = (
        capo_bedrock_agentcore_control.types.policy_status_reasons.serialize_json(
            value["status_reasons"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPolicyGenerationResponse:
    out: GetPolicyGenerationResponse = {}  # type: ignore[typeddict-item]
    if "policyEngineId" in data:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        raise DeserializationError(
            "GetPolicyGenerationResponse.policy_engine_id required"
        )
    if "policyGenerationId" in data:
        out["policy_generation_id"] = data["policyGenerationId"]
    else:
        raise DeserializationError(
            "GetPolicyGenerationResponse.policy_generation_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPolicyGenerationResponse.name required")
    if "policyGenerationArn" in data:
        out["policy_generation_arn"] = data["policyGenerationArn"]
    else:
        raise DeserializationError(
            "GetPolicyGenerationResponse.policy_generation_arn required"
        )
    if "resource" in data:
        import capo_bedrock_agentcore_control.types.resource

        out["resource"] = (
            capo_bedrock_agentcore_control.types.resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("GetPolicyGenerationResponse.resource required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicyGenerationResponse.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicyGenerationResponse.updated_at required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.policy_generation_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_generation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetPolicyGenerationResponse.status required")
    if "findings" in data:
        out["findings"] = data["findings"]
    if "statusReasons" in data:
        import capo_bedrock_agentcore_control.types.policy_status_reasons

        out["status_reasons"] = (
            capo_bedrock_agentcore_control.types.policy_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    else:
        raise DeserializationError(
            "GetPolicyGenerationResponse.status_reasons required"
        )
    return out
