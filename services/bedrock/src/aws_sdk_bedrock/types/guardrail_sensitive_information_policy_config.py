"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSensitiveInformationPolicyConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_pii_entities_config
    import aws_sdk_bedrock.types.guardrail_regexes_config


class GuardrailSensitiveInformationPolicyConfig(TypedDict):
    pii_entities_config: NotRequired[
        "aws_sdk_bedrock.types.guardrail_pii_entities_config.GuardrailPiiEntitiesConfig"
    ]
    """<p>A list of PII entities to configure to the guardrail.</p>"""
    regexes_config: NotRequired[
        "aws_sdk_bedrock.types.guardrail_regexes_config.GuardrailRegexesConfig"
    ]
    """<p>A list of regular expressions to configure to the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicyConfig) -> dict:
    out: dict = {}
    if "pii_entities_config" in value:
        import aws_sdk_bedrock.types.guardrail_pii_entities_config

        out["piiEntitiesConfig"] = (
            aws_sdk_bedrock.types.guardrail_pii_entities_config.serialize_json(
                value["pii_entities_config"]
            )
        )
    if "regexes_config" in value:
        import aws_sdk_bedrock.types.guardrail_regexes_config

        out["regexesConfig"] = (
            aws_sdk_bedrock.types.guardrail_regexes_config.serialize_json(
                value["regexes_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailSensitiveInformationPolicyConfig:
    out: GuardrailSensitiveInformationPolicyConfig = {}  # type: ignore[typeddict-item]
    if "piiEntitiesConfig" in data:
        import aws_sdk_bedrock.types.guardrail_pii_entities_config

        out["pii_entities_config"] = (
            aws_sdk_bedrock.types.guardrail_pii_entities_config.deserialize_json(
                data["piiEntitiesConfig"]
            )
        )
    if "regexesConfig" in data:
        import aws_sdk_bedrock.types.guardrail_regexes_config

        out["regexes_config"] = (
            aws_sdk_bedrock.types.guardrail_regexes_config.deserialize_json(
                data["regexesConfig"]
            )
        )
    return out
