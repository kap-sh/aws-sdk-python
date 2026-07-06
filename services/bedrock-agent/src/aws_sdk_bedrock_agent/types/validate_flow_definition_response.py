"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ValidateFlowDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_validations


class ValidateFlowDefinitionResponse(TypedDict, closed=True):
    validations: "aws_sdk_bedrock_agent.types.flow_validations.FlowValidations"
    """<p>Contains an array of objects, each of which contains an error identified by validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateFlowDefinitionResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.flow_validations

    out["validations"] = aws_sdk_bedrock_agent.types.flow_validations.serialize_json(
        value["validations"]
    )
    return out


def deserialize_json(data: dict) -> ValidateFlowDefinitionResponse:
    out: ValidateFlowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "validations" in data:
        import aws_sdk_bedrock_agent.types.flow_validations

        out["validations"] = (
            aws_sdk_bedrock_agent.types.flow_validations.deserialize_json(
                data["validations"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateFlowDefinitionResponse.validations required"
        )
    return out
