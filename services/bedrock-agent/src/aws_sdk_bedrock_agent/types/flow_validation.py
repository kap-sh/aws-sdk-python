"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_validation_details
    import aws_sdk_bedrock_agent.types.flow_validation_severity
    import aws_sdk_bedrock_agent.types.flow_validation_type
    import aws_sdk_bedrock_agent.types.non_blank_string


class FlowValidation(TypedDict):
    message: "aws_sdk_bedrock_agent.types.non_blank_string.NonBlankString"
    """<p>A message describing the validation error.</p>"""
    severity: (
        "aws_sdk_bedrock_agent.types.flow_validation_severity.FlowValidationSeverity"
    )
    """<p>The severity of the issue described in the message.</p>"""
    details: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_validation_details.FlowValidationDetails"
    ]
    """<p>Specific details about the validation issue encountered in the flow.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_validation_type.FlowValidationType"
    ]
    """<p>The type of validation issue encountered in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidation) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_bedrock_agent.types.flow_validation_severity

    out["severity"] = (
        aws_sdk_bedrock_agent.types.flow_validation_severity.serialize_json(
            value["severity"]
        )
    )
    if "details" in value:
        import aws_sdk_bedrock_agent.types.flow_validation_details

        out["details"] = (
            aws_sdk_bedrock_agent.types.flow_validation_details.serialize_json(
                value["details"]
            )
        )
    if "type" in value:
        import aws_sdk_bedrock_agent.types.flow_validation_type

        out["type"] = aws_sdk_bedrock_agent.types.flow_validation_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> FlowValidation:
    out: FlowValidation = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("FlowValidation.message required")
    if "severity" in data:
        import aws_sdk_bedrock_agent.types.flow_validation_severity

        out["severity"] = (
            aws_sdk_bedrock_agent.types.flow_validation_severity.deserialize_json(
                data["severity"]
            )
        )
    else:
        raise DeserializationError("FlowValidation.severity required")
    if "details" in data:
        import aws_sdk_bedrock_agent.types.flow_validation_details

        out["details"] = (
            aws_sdk_bedrock_agent.types.flow_validation_details.deserialize_json(
                data["details"]
            )
        )
    if "type" in data:
        import aws_sdk_bedrock_agent.types.flow_validation_type

        out["type"] = aws_sdk_bedrock_agent.types.flow_validation_type.deserialize_json(
            data["type"]
        )
    return out
