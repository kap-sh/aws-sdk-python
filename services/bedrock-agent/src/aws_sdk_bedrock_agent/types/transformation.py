"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Transformation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.step_type
    import aws_sdk_bedrock_agent.types.transformation_function


class Transformation(TypedDict):
    transformation_function: (
        "aws_sdk_bedrock_agent.types.transformation_function.TransformationFunction"
    )
    """<p>A Lambda function that processes documents.</p>"""
    step_to_apply: "aws_sdk_bedrock_agent.types.step_type.StepType"
    """<p>When the service applies the transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transformation) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.transformation_function

    out["transformationFunction"] = (
        aws_sdk_bedrock_agent.types.transformation_function.serialize_json(
            value["transformation_function"]
        )
    )
    import aws_sdk_bedrock_agent.types.step_type

    out["stepToApply"] = aws_sdk_bedrock_agent.types.step_type.serialize_json(
        value["step_to_apply"]
    )
    return out


def deserialize_json(data: dict) -> Transformation:
    out: Transformation = {}  # type: ignore[typeddict-item]
    if "transformationFunction" in data:
        import aws_sdk_bedrock_agent.types.transformation_function

        out["transformation_function"] = (
            aws_sdk_bedrock_agent.types.transformation_function.deserialize_json(
                data["transformationFunction"]
            )
        )
    else:
        raise DeserializationError("Transformation.transformation_function required")
    if "stepToApply" in data:
        import aws_sdk_bedrock_agent.types.step_type

        out["step_to_apply"] = aws_sdk_bedrock_agent.types.step_type.deserialize_json(
            data["stepToApply"]
        )
    else:
        raise DeserializationError("Transformation.step_to_apply required")
    return out
