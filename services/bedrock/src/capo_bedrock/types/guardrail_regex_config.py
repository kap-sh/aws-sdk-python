"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailRegexConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_sensitive_information_action


class GuardrailRegexConfig(TypedDict, closed=True):
    name: "str"
    """<p>The name of the regular expression to configure for the guardrail.</p>"""
    description: NotRequired["str"]
    """<p>The description of the regular expression to configure for the guardrail.</p>"""
    pattern: "str"
    """<p>The regular expression pattern to configure for the guardrail.</p>"""
    action: "capo_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    """<p>The guardrail action to configure when matching regular expression is detected.</p>"""
    input_action: NotRequired[
        "capo_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>Specifies the action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "capo_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>Specifies the action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexConfig) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["pattern"] = value["pattern"]
    import capo_bedrock.types.guardrail_sensitive_information_action

    out["action"] = (
        capo_bedrock.types.guardrail_sensitive_information_action.serialize_json(
            value["action"]
        )
    )
    if "input_action" in value:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["inputAction"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.serialize_json(
                value["input_action"]
            )
        )
    if "output_action" in value:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["outputAction"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.serialize_json(
                value["output_action"]
            )
        )
    if "input_enabled" in value:
        out["inputEnabled"] = value["input_enabled"]
    if "output_enabled" in value:
        out["outputEnabled"] = value["output_enabled"]
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
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["action"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailRegexConfig.action required")
    if "inputAction" in data:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["input_action"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["inputAction"]
            )
        )
    if "outputAction" in data:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["output_action"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["outputAction"]
            )
        )
    if "inputEnabled" in data:
        out["input_enabled"] = data["inputEnabled"]
    if "outputEnabled" in data:
        out["output_enabled"] = data["outputEnabled"]
    return out
