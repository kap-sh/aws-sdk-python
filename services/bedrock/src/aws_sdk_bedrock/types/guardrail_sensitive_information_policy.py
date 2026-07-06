"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSensitiveInformationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_pii_entities
    import aws_sdk_bedrock.types.guardrail_regexes


class GuardrailSensitiveInformationPolicy(TypedDict, closed=True):
    pii_entities: NotRequired[
        "aws_sdk_bedrock.types.guardrail_pii_entities.GuardrailPiiEntities"
    ]
    """<p>The list of PII entities configured for the guardrail.</p>"""
    regexes: NotRequired["aws_sdk_bedrock.types.guardrail_regexes.GuardrailRegexes"]
    """<p>The list of regular expressions configured for the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicy) -> dict:
    out: dict = {}
    if "pii_entities" in value:
        import aws_sdk_bedrock.types.guardrail_pii_entities

        out["piiEntities"] = (
            aws_sdk_bedrock.types.guardrail_pii_entities.serialize_json(
                value["pii_entities"]
            )
        )
    if "regexes" in value:
        import aws_sdk_bedrock.types.guardrail_regexes

        out["regexes"] = aws_sdk_bedrock.types.guardrail_regexes.serialize_json(
            value["regexes"]
        )
    return out


def deserialize_json(data: dict) -> GuardrailSensitiveInformationPolicy:
    out: GuardrailSensitiveInformationPolicy = {}  # type: ignore[typeddict-item]
    if "piiEntities" in data:
        import aws_sdk_bedrock.types.guardrail_pii_entities

        out["pii_entities"] = (
            aws_sdk_bedrock.types.guardrail_pii_entities.deserialize_json(
                data["piiEntities"]
            )
        )
    if "regexes" in data:
        import aws_sdk_bedrock.types.guardrail_regexes

        out["regexes"] = aws_sdk_bedrock.types.guardrail_regexes.deserialize_json(
            data["regexes"]
        )
    return out
