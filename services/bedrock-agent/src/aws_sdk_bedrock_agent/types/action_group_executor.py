"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ActionGroupExecutor``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.custom_control_method
    import aws_sdk_bedrock_agent.types.lambda_arn

_ActionGroupExecutor_lambda = TypedDict(
    "_ActionGroupExecutor_lambda",
    {
        "lambda": "aws_sdk_bedrock_agent.types.lambda_arn.LambdaArn",
    },
    closed=True,
)


class _ActionGroupExecutor_customControl(TypedDict, closed=True):
    customControl: (
        "aws_sdk_bedrock_agent.types.custom_control_method.CustomControlMethod"
    )


ActionGroupExecutor: TypeAlias = (
    _ActionGroupExecutor_lambda | _ActionGroupExecutor_customControl
)


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupExecutor) -> dict:
    if "lambda" in value:
        return {"lambda": value["lambda"]}
    elif "customControl" in value:
        import aws_sdk_bedrock_agent.types.custom_control_method

        return {
            "customControl": aws_sdk_bedrock_agent.types.custom_control_method.serialize_json(
                value["customControl"]
            )
        }
    else:
        raise SerializationError("ActionGroupExecutor: no variant present")


def deserialize_json(data: dict) -> ActionGroupExecutor:
    if "lambda" in data:
        return {"lambda": data["lambda"]}
    elif "customControl" in data:
        import aws_sdk_bedrock_agent.types.custom_control_method

        return {
            "customControl": aws_sdk_bedrock_agent.types.custom_control_method.deserialize_json(
                data["customControl"]
            )
        }
    else:
        raise DeserializationError("ActionGroupExecutor: no recognized variant key")
