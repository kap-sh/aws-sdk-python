"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailRegex``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_sensitive_information_action


class GuardrailRegex(TypedDict):
    name: "str"
    """<p>The name of the regular expression for the guardrail.</p>"""
    description: NotRequired["str"]
    """<p>The description of the regular expression for the guardrail.</p>"""
    pattern: "str"
    """<p>The pattern of the regular expression configured for the guardrail.</p>"""
    action: "aws_sdk_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    """<p>The action taken when a match to the regular expression is detected.</p>"""
    input_action: NotRequired[
        "aws_sdk_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>The action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "aws_sdk_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>The action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegex) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["pattern"] = value["pattern"]
    import aws_sdk_bedrock.types.guardrail_sensitive_information_action

    out["action"] = (
        aws_sdk_bedrock.types.guardrail_sensitive_information_action.serialize_json(
            value["action"]
        )
    )
    if "input_action" in value:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_action

        out["inputAction"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_action.serialize_json(
                value["input_action"]
            )
        )
    if "output_action" in value:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_action

        out["outputAction"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_action.serialize_json(
                value["output_action"]
            )
        )
    if "input_enabled" in value:
        out["inputEnabled"] = value["input_enabled"]
    if "output_enabled" in value:
        out["outputEnabled"] = value["output_enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailRegex:
    out: GuardrailRegex = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GuardrailRegex.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "pattern" in data:
        out["pattern"] = data["pattern"]
    else:
        raise DeserializationError("GuardrailRegex.pattern required")
    if "action" in data:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_action

        out["action"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailRegex.action required")
    if "inputAction" in data:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_action

        out["input_action"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["inputAction"]
            )
        )
    if "outputAction" in data:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_action

        out["output_action"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["outputAction"]
            )
        )
    if "inputEnabled" in data:
        out["input_enabled"] = data["inputEnabled"]
    if "outputEnabled" in data:
        out["output_enabled"] = data["outputEnabled"]
    return out
