"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailRegexFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action


class GuardrailRegexFilter(TypedDict):
    name: NotRequired["str"]
    """<p>The name details for the regex filter used in the Guardrail.</p>"""
    regex: NotRequired["str"]
    """<p>The regex details for the regex filter used in the Guardrail.</p>"""
    match: NotRequired["str"]
    """<p>The match details for the regex filter used in the Guardrail.</p>"""
    action: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action.GuardrailSensitiveInformationPolicyAction"
    ]
    """<p>The action details for the regex filter used in the Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "regex" in value:
        out["regex"] = value["regex"]
    if "match" in value:
        out["match"] = value["match"]
    if "action" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailRegexFilter:
    out: GuardrailRegexFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "regex" in data:
        out["regex"] = data["regex"]
    if "match" in data:
        out["match"] = data["match"]
    if "action" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_sensitive_information_policy_action.deserialize_json(
                data["action"]
            )
        )
    return out
