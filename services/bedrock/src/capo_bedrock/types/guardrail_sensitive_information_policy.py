"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSensitiveInformationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_pii_entities
    import capo_bedrock.types.guardrail_regexes


class GuardrailSensitiveInformationPolicy(TypedDict, closed=True):
    pii_entities: NotRequired[
        "capo_bedrock.types.guardrail_pii_entities.GuardrailPiiEntities"
    ]
    """<p>The list of PII entities configured for the guardrail.</p>"""
    regexes: NotRequired["capo_bedrock.types.guardrail_regexes.GuardrailRegexes"]
    """<p>The list of regular expressions configured for the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicy) -> dict:
    out: dict = {}
    if "pii_entities" in value:
        import capo_bedrock.types.guardrail_pii_entities

        out["piiEntities"] = capo_bedrock.types.guardrail_pii_entities.serialize_json(
            value["pii_entities"]
        )
    if "regexes" in value:
        import capo_bedrock.types.guardrail_regexes

        out["regexes"] = capo_bedrock.types.guardrail_regexes.serialize_json(
            value["regexes"]
        )
    return out


def deserialize_json(data: dict) -> GuardrailSensitiveInformationPolicy:
    out: GuardrailSensitiveInformationPolicy = {}  # type: ignore[typeddict-item]
    if "piiEntities" in data:
        import capo_bedrock.types.guardrail_pii_entities

        out["pii_entities"] = (
            capo_bedrock.types.guardrail_pii_entities.deserialize_json(
                data["piiEntities"]
            )
        )
    if "regexes" in data:
        import capo_bedrock.types.guardrail_regexes

        out["regexes"] = capo_bedrock.types.guardrail_regexes.deserialize_json(
            data["regexes"]
        )
    return out
