"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OrchestrationExecutor``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.lambda_arn

_OrchestrationExecutor_lambda = TypedDict(
    "_OrchestrationExecutor_lambda",
    {
        "lambda": "aws_sdk_bedrock_agent_runtime.types.lambda_arn.LambdaArn",
    },
    closed=True,
)

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
