"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.policy_definition
    import capo_bedrock_agentcore_control.types.policy_validation_mode
    import capo_bedrock_agentcore_control.types.resource_id
    import capo_bedrock_agentcore_control.types.updated_description


class UpdatePolicyRequest(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine that manages the policy to be updated. This ensures the policy is updated within the correct policy engine context.</p>"""
    policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy to be updated. This must be a valid policy ID that exists within the specified policy engine.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
    ]
    """<p>The new human-readable description for the policy. This optional field allows updating the policy's documentation while keeping the same policy logic.</p>"""
    definition: NotRequired[
        "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    ]
    """<p>The new Cedar policy statement that defines the access control rules. This replaces the existing policy definition with new logic while maintaining the policy's identity.</p>"""
    validation_mode: "capo_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"
    """<p>The validation mode for the policy update. Determines how Cedar analyzer validation results are handled during policy updates. FAIL_ON_ANY_FINDINGS runs the Cedar analyzer and fails the update if validation issues are detected, ensuring the policy conforms to the Cedar schema and tool context. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows updates despite validation warnings. Use FAIL_ON_ANY_FINDINGS to ensure policy correctness during updates, especially when modifying policy logic or conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyRequest) -> dict:
    out: dict = {}
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.serialize_json(
                value["description"]
            )
        )
    if "definition" in value:
        import capo_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            capo_bedrock_agentcore_control.types.policy_definition.serialize_json(
                value["definition"]
            )
        )
    import capo_bedrock_agentcore_control.types.policy_validation_mode

    out["validationMode"] = (
        capo_bedrock_agentcore_control.types.policy_validation_mode.serialize_json(
            value.get("validation_mode", "FAIL_ON_ANY_FINDINGS")
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePolicyRequest:
    out: UpdatePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.deserialize_json(
                data["description"]
            )
        )
    if data.get("definition") is not None:
        import capo_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            capo_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    if data.get("validationMode") is not None:
        import capo_bedrock_agentcore_control.types.policy_validation_mode

        out["validation_mode"] = (
            capo_bedrock_agentcore_control.types.policy_validation_mode.deserialize_json(
                data["validationMode"]
            )
        )
    else:
        out["validation_mode"] = "FAIL_ON_ANY_FINDINGS"
    return out
