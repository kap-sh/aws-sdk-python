"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailPiiEntityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_pii_entity_type
    import capo_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action


class GuardrailPiiEntityFilter(TypedDict, closed=True):
    type: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_pii_entity_type.GuardrailPiiEntityType"
    ]
    """<p>The type of PII the Guardrail filter has identified and removed.</p>"""
    match: NotRequired["str"]
    """<p>The match to settings in the Guardrail filter to identify and remove PII.</p>"""
    action: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action.GuardrailSensitiveInformationPolicyAction"
    ]
    """<p>The action of the Guardrail filter to identify and remove PII.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntityFilter) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_bedrock_agent_runtime.types.guardrail_pii_entity_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.guardrail_pii_entity_type.serialize_json(
                value["type"]
            )
        )
    if "match" in value:
        out["match"] = value["match"]
    if "action" in value:
        import capo_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailPiiEntityFilter:
    out: GuardrailPiiEntityFilter = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_pii_entity_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.guardrail_pii_entity_type.deserialize_json(
                data["type"]
            )
        )
    if data.get("match") is not None:
        out["match"] = data["match"]
    if data.get("action") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
