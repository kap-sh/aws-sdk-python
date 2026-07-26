"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailRegexFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action


class GuardrailRegexFilter(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The regex filter name.</p>"""
    match: NotRequired["str"]
    """<p>The regesx filter match.</p>"""
    regex: NotRequired["str"]
    """<p>The regex query.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.GuardrailSensitiveInformationPolicyAction"
    """<p>The region filter action.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether custom regex entities that breach the guardrail configuration are detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "match" in value:
        out["match"] = value["match"]
    if "regex" in value:
        out["regex"] = value["regex"]
    import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action

    out["action"] = (
        capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailRegexFilter:
    out: GuardrailRegexFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "match" in data:
        out["match"] = data["match"]
    if "regex" in data:
        out["regex"] = data["regex"]
    if "action" in data:
        import capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action

        out["action"] = (
            capo_bedrock_runtime.types.guardrail_sensitive_information_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailRegexFilter.action required")
    if "detected" in data:
        out["detected"] = data["detected"]
    return out
