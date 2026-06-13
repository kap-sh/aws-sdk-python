"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailSensitiveInformationPolicyAssessment``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter_list
    import aws_sdk_bedrock_runtime.types.guardrail_regex_filter_list


class GuardrailSensitiveInformationPolicyAssessment(TypedDict):
    pii_entities: "aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter_list.GuardrailPiiEntityFilterList"
    """<p>The PII entities in the assessment.</p>"""
    regexes: "aws_sdk_bedrock_runtime.types.guardrail_regex_filter_list.GuardrailRegexFilterList"
    """<p>The regex queries in the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicyAssessment) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter_list

    out["piiEntities"] = (
        aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter_list.serialize_json(
            value["pii_entities"]
        )
    )
    import aws_sdk_bedrock_runtime.types.guardrail_regex_filter_list

    out["regexes"] = (
        aws_sdk_bedrock_runtime.types.guardrail_regex_filter_list.serialize_json(
            value["regexes"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailSensitiveInformationPolicyAssessment:
    out: GuardrailSensitiveInformationPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "piiEntities" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter_list

        out["pii_entities"] = (
            aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter_list.deserialize_json(
                data["piiEntities"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailSensitiveInformationPolicyAssessment.pii_entities required"
        )
    if "regexes" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_regex_filter_list

        out["regexes"] = (
            aws_sdk_bedrock_runtime.types.guardrail_regex_filter_list.deserialize_json(
                data["regexes"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailSensitiveInformationPolicyAssessment.regexes required"
        )
    return out
