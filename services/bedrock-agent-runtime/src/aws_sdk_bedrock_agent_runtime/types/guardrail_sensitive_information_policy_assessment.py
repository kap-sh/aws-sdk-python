"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailSensitiveInformationPolicyAssessment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_pii_entity_filter_list
    import aws_sdk_bedrock_agent_runtime.types.guardrail_regex_filter_list


class GuardrailSensitiveInformationPolicyAssessment(TypedDict):
    pii_entities: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_pii_entity_filter_list.GuardrailPiiEntityFilterList"
    ]
    """<p>The details of the PII entities used in the sensitive policy assessment for the Guardrail.</p>"""
    regexes: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_regex_filter_list.GuardrailRegexFilterList"
    ]
    """<p>The details of the regexes used in the sensitive policy assessment for the Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicyAssessment) -> dict:
    out: dict = {}
    if "pii_entities" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_pii_entity_filter_list

        out["piiEntities"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_pii_entity_filter_list.serialize_json(
                value["pii_entities"]
            )
        )
    if "regexes" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_regex_filter_list

        out["regexes"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_regex_filter_list.serialize_json(
                value["regexes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailSensitiveInformationPolicyAssessment:
    out: GuardrailSensitiveInformationPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "piiEntities" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_pii_entity_filter_list

        out["pii_entities"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_pii_entity_filter_list.deserialize_json(
                data["piiEntities"]
            )
        )
    if "regexes" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_regex_filter_list

        out["regexes"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_regex_filter_list.deserialize_json(
                data["regexes"]
            )
        )
    return out
