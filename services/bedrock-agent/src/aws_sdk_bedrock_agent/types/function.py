"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Function``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.function_description
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.parameter_map
    import aws_sdk_bedrock_agent.types.require_confirmation


class Function(TypedDict):
    name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>A name for the function.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.function_description.FunctionDescription"
    ]
    """<p>A description of the function and its purpose.</p>"""
    parameters: NotRequired["aws_sdk_bedrock_agent.types.parameter_map.ParameterMap"]
    """<p>The parameters that the agent elicits from the user to fulfill the function.</p>"""
    require_confirmation: NotRequired[
        "aws_sdk_bedrock_agent.types.require_confirmation.RequireConfirmation"
    ]
    """<p>Contains information if user confirmation is required to invoke the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Function) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import aws_sdk_bedrock_agent.types.parameter_map

        out["parameters"] = aws_sdk_bedrock_agent.types.parameter_map.serialize_json(
            value["parameters"]
        )
    if "require_confirmation" in value:
        import aws_sdk_bedrock_agent.types.require_confirmation

        out["requireConfirmation"] = (
            aws_sdk_bedrock_agent.types.require_confirmation.serialize_json(
                value["require_confirmation"]
            )
        )
    return out


def deserialize_json(data: dict) -> Function:
    out: Function = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Function.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "parameters" in data:
        import aws_sdk_bedrock_agent.types.parameter_map

        out["parameters"] = aws_sdk_bedrock_agent.types.parameter_map.deserialize_json(
            data["parameters"]
        )
    if "requireConfirmation" in data:
        import aws_sdk_bedrock_agent.types.require_confirmation

        out["require_confirmation"] = (
            aws_sdk_bedrock_agent.types.require_confirmation.deserialize_json(
                data["requireConfirmation"]
            )
        )
    return out
