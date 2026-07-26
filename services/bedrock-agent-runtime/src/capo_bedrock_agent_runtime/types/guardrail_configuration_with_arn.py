"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailConfigurationWithArn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_identifier_with_arn
    import capo_bedrock_agent_runtime.types.guardrail_version


class GuardrailConfigurationWithArn(TypedDict, closed=True):
    guardrail_identifier: "capo_bedrock_agent_runtime.types.guardrail_identifier_with_arn.GuardrailIdentifierWithArn"
    """<p> The unique identifier for the guardrail. </p>"""
    guardrail_version: (
        "capo_bedrock_agent_runtime.types.guardrail_version.GuardrailVersion"
    )
    """<p> The version of the guardrail. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConfigurationWithArn) -> dict:
    out: dict = {}
    out["guardrailIdentifier"] = value["guardrail_identifier"]
    out["guardrailVersion"] = value["guardrail_version"]
    return out


def deserialize_json(data: dict) -> GuardrailConfigurationWithArn:
    out: GuardrailConfigurationWithArn = {}  # type: ignore[typeddict-item]
    if "guardrailIdentifier" in data:
        out["guardrail_identifier"] = data["guardrailIdentifier"]
    else:
        raise DeserializationError(
            "GuardrailConfigurationWithArn.guardrail_identifier required"
        )
    if "guardrailVersion" in data:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        raise DeserializationError(
            "GuardrailConfigurationWithArn.guardrail_version required"
        )
    return out
