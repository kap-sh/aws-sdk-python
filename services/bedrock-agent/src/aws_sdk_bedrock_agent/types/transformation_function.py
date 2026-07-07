"""Generated from Smithy shape ``com.amazonaws.bedrockagent#TransformationFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.transformation_lambda_configuration


class TransformationFunction(TypedDict, closed=True):
    transformation_lambda_configuration: "aws_sdk_bedrock_agent.types.transformation_lambda_configuration.TransformationLambdaConfiguration"
    """<p>The Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformationFunction) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.transformation_lambda_configuration

    out["transformationLambdaConfiguration"] = (
        aws_sdk_bedrock_agent.types.transformation_lambda_configuration.serialize_json(
            value["transformation_lambda_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> TransformationFunction:
    out: TransformationFunction = {}  # type: ignore[typeddict-item]
    if "transformationLambdaConfiguration" in data:
        import aws_sdk_bedrock_agent.types.transformation_lambda_configuration

        out["transformation_lambda_configuration"] = (
            aws_sdk_bedrock_agent.types.transformation_lambda_configuration.deserialize_json(
                data["transformationLambdaConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "TransformationFunction.transformation_lambda_configuration required"
        )
    return out
