"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailRegexConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_regex_description
    import aws_sdk_qconnect.types.guardrail_regex_name
    import aws_sdk_qconnect.types.guardrail_regex_pattern
    import aws_sdk_qconnect.types.guardrail_sensitive_information_action


class GuardrailRegexConfig(TypedDict):
    name: "aws_sdk_qconnect.types.guardrail_regex_name.GuardrailRegexName"
    """<p>The name of the regular expression to configure for the AI Guardrail.</p>"""
    description: NotRequired[
        "aws_sdk_qconnect.types.guardrail_regex_description.GuardrailRegexDescription"
    ]
    """<p>The description of the regular expression to configure for the AI Guardrail.</p>"""
    pattern: "aws_sdk_qconnect.types.guardrail_regex_pattern.GuardrailRegexPattern"
    """<p>The regular expression pattern to configure for the AI Guardrail.</p>"""
    action: "aws_sdk_qconnect.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    """<p>The AI Guardrail action to configure when matching regular expression is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexConfig) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["pattern"] = value["pattern"]
    out["action"] = value["action"]
    return out


def deserialize_json(data: dict) -> GuardrailRegexConfig:
    out: GuardrailRegexConfig = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GuardrailRegexConfig.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "pattern" in data:
        out["pattern"] = data["pattern"]
    else:
        raise DeserializationError("GuardrailRegexConfig.pattern required")
    if "action" in data:
        out["action"] = data["action"]
    else:
        raise DeserializationError("GuardrailRegexConfig.action required")
    return out
