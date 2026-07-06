"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailPiiEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_pii_entity_type
    import aws_sdk_bedrock.types.guardrail_sensitive_information_action


class GuardrailPiiEntity(TypedDict, closed=True):
    type: "aws_sdk_bedrock.types.guardrail_pii_entity_type.GuardrailPiiEntityType"
    """<p>The type of PII entity. For example, Social Security Number.</p>"""
    action: "aws_sdk_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    """<p>The configured guardrail action when PII entity is detected.</p>"""
    input_action: NotRequired[
        "aws_sdk_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>The action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>ANONYMIZE</code> – Mask the content and replace it with identifier tags.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "aws_sdk_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>The action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>ANONYMIZE</code> – Mask the content and replace it with identifier tags.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntity) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.guardrail_pii_entity_type

    out["type"] = aws_sdk_bedrock.types.guardrail_pii_entity_type.serialize_json(
        value["type"]
    )
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


def deserialize_json(data: dict) -> GuardrailPiiEntity:
    out: GuardrailPiiEntity = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock.types.guardrail_pii_entity_type

        out["type"] = aws_sdk_bedrock.types.guardrail_pii_entity_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GuardrailPiiEntity.type required")
    if "action" in data:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_action

        out["action"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("GuardrailPiiEntity.action required")
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
