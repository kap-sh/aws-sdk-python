"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.policy_definition
    import aws_sdk_bedrock_agentcore_control.types.policy_name
    import aws_sdk_bedrock_agentcore_control.types.policy_validation_mode
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class CreatePolicyRequest(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agentcore_control.types.policy_name.PolicyName"
    """<p>The customer-assigned immutable name for the policy. Must be unique within the account. This name is used for policy identification and cannot be changed after creation.</p>"""
    definition: (
        "aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    )
    """<p>The Cedar policy statement that defines the access control rules. This contains the actual policy logic written in Cedar policy language, specifying effect (permit or forbid), principals, actions, resources, and conditions for agent behavior control.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>A human-readable description of the policy's purpose and functionality (1-4,096 characters). This helps policy administrators understand the policy's intent, business rules, and operational scope. Use this field to document why the policy exists, what business requirement it addresses, and any special considerations for maintenance. Clear descriptions are essential for policy governance, auditing, and troubleshooting.</p>"""
    validation_mode: "aws_sdk_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"
    """<p>The validation mode for the policy creation. Determines how Cedar analyzer validation results are handled during policy creation. FAIL_ON_ANY_FINDINGS (default) runs the Cedar analyzer to validate the policy against the Cedar schema and tool context, failing creation if the analyzer detects any validation issues to ensure strict conformance. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows policy creation even if validation issues are detected, useful for testing or when the policy schema is evolving. Use FAIL_ON_ANY_FINDINGS for production policies to ensure correctness, and IGNORE_ALL_FINDINGS only when you understand and accept the analyzer findings.</p>"""
    policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine which contains this policy. Policy engines group related policies and provide the execution context for policy evaluation.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.policy_definition

    out["definition"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_definition.serialize_json(
            value["definition"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.policy_validation_mode

    out["validationMode"] = (
        aws_sdk_bedrock_agentcore_control.types.policy_validation_mode.serialize_json(
            value.get("validation_mode", "FAIL_ON_ANY_FINDINGS")
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePolicyRequest:
    out: CreatePolicyRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePolicyRequest.name required")
    if "definition" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyRequest.definition required")
    if "description" in data:
        out["description"] = data["description"]
    if "validationMode" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_validation_mode

        out["validation_mode"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_validation_mode.deserialize_json(
                data["validationMode"]
            )
        )
    else:
        out["validation_mode"] = "FAIL_ON_ANY_FINDINGS"
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
