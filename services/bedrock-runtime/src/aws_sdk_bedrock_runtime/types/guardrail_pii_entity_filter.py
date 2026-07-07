"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailPiiEntityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_type
    import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_action


class GuardrailPiiEntityFilter(TypedDict, closed=True):
    match: "str"
    """<p>The PII entity filter match.</p>"""
    type: (
        "aws_sdk_bedrock_runtime.types.guardrail_pii_entity_type.GuardrailPiiEntityType"
    )
    """<p>The PII entity filter type.</p>"""
    action: "aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_action.GuardrailSensitiveInformationPolicyAction"
    """<p>The PII entity filter action.</p>"""
    detected: NotRequired["bool"]
    """<p>Indicates whether personally identifiable information (PII) that breaches the guardrail configuration is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntityFilter) -> dict:
    out: dict = {}
    out["match"] = value["match"]
    import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_type

    out["type"] = (
        aws_sdk_bedrock_runtime.types.guardrail_pii_entity_type.serialize_json(
            value["type"]
        )
    )
    import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_action

    out["action"] = (
        aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_action.serialize_json(
            value["action"]
        )
    )
    if "detected" in value:
        out["detected"] = value["detected"]
    return out


def deserialize_json(data: dict) -> GuardrailPiiEntityFilter:
    out: GuardrailPiiEntityFilter = {}  # type: ignore[typeddict-item]
    if "match" in data:
        out["match"] = data["match"]
    else:
        raise DeserializationError("GuardrailPiiEntityFilter.match required")
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_type

        out["type"] = (
            aws_sdk_bedrock_runtime.types.guardrail_pii_entity_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("GuardrailPiiEntityFilter.type required")
    if "action" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_action

        out["action"] = (
            aws_sdk_bedrock_runtime.types.guardrail_sensitive_information_policy_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailPiiEntityFilter.action required")
    if "detected" in data:
        out["detected"] = data["detected"]
    return out
