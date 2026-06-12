"""Generated from Smithy shape ``com.amazonaws.bedrockagent#OrchestrationExecutor``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    pass


class _OrchestrationExecutor_lambda(TypedDict):
    lambda: "aws_sdk_bedrock_agent.types.lambda_arn.LambdaArn"


OrchestrationExecutor: TypeAlias = _OrchestrationExecutor_lambda


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationExecutor) -> dict:
    if "lambda" in value:
        return {"lambda": value["lambda"]}
    else:
        raise SerializationError("OrchestrationExecutor: no variant present")


def deserialize_json(data: dict) -> OrchestrationExecutor:
    if "lambda" in data:
        return {"lambda": data["lambda"]}
    else:
        raise DeserializationError("OrchestrationExecutor: no recognized variant key")
