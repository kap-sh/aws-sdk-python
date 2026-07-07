"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GuardrailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.guardrail_identifier
    import aws_sdk_bedrock_agent.types.guardrail_version


class GuardrailConfiguration(TypedDict, closed=True):
    guardrail_identifier: NotRequired[
        "aws_sdk_bedrock_agent.types.guardrail_identifier.GuardrailIdentifier"
    ]
    """<p>The unique identifier of the guardrail.</p>"""
    guardrail_version: NotRequired[
        "aws_sdk_bedrock_agent.types.guardrail_version.GuardrailVersion"
    ]
    """<p>The version of the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConfiguration) -> dict:
    out: dict = {}
    if "guardrail_identifier" in value:
        out["guardrailIdentifier"] = value["guardrail_identifier"]
    if "guardrail_version" in value:
        out["guardrailVersion"] = value["guardrail_version"]
    return out


def deserialize_json(data: dict) -> GuardrailConfiguration:
    out: GuardrailConfiguration = {}  # type: ignore[typeddict-item]
    if "guardrailIdentifier" in data:
        out["guardrail_identifier"] = data["guardrailIdentifier"]
    if "guardrailVersion" in data:
        out["guardrail_version"] = data["guardrailVersion"]
    return out
