"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailSensitiveInformationPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_pii_entities_config
    import aws_sdk_qconnect.types.guardrail_regexes_config


class AIGuardrailSensitiveInformationPolicyConfig(TypedDict, closed=True):
    pii_entities_config: NotRequired[
        "aws_sdk_qconnect.types.guardrail_pii_entities_config.GuardrailPiiEntitiesConfig"
    ]
    """<p>A list of PII entities to configure to the AI Guardrail.</p>"""
    regexes_config: NotRequired[
        "aws_sdk_qconnect.types.guardrail_regexes_config.GuardrailRegexesConfig"
    ]
    """<p>A list of regular expressions to configure to the AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailSensitiveInformationPolicyConfig) -> dict:
    out: dict = {}
    if "pii_entities_config" in value:
        import aws_sdk_qconnect.types.guardrail_pii_entities_config

        out["piiEntitiesConfig"] = (
            aws_sdk_qconnect.types.guardrail_pii_entities_config.serialize_json(
                value["pii_entities_config"]
            )
        )
    if "regexes_config" in value:
        import aws_sdk_qconnect.types.guardrail_regexes_config

        out["regexesConfig"] = (
            aws_sdk_qconnect.types.guardrail_regexes_config.serialize_json(
                value["regexes_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AIGuardrailSensitiveInformationPolicyConfig:
    out: AIGuardrailSensitiveInformationPolicyConfig = {}  # type: ignore[typeddict-item]
    if "piiEntitiesConfig" in data:
        import aws_sdk_qconnect.types.guardrail_pii_entities_config

        out["pii_entities_config"] = (
            aws_sdk_qconnect.types.guardrail_pii_entities_config.deserialize_json(
                data["piiEntitiesConfig"]
            )
        )
    if "regexesConfig" in data:
        import aws_sdk_qconnect.types.guardrail_regexes_config

        out["regexes_config"] = (
            aws_sdk_qconnect.types.guardrail_regexes_config.deserialize_json(
                data["regexesConfig"]
            )
        )
    return out
