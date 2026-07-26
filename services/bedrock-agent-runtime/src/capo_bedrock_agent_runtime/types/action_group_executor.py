"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupExecutor``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.custom_control_method
    import capo_bedrock_agent_runtime.types.lambda_resource_arn

_ActionGroupExecutor_lambda = TypedDict(
    "_ActionGroupExecutor_lambda",
    {
        "lambda": "capo_bedrock_agent_runtime.types.lambda_resource_arn.LambdaResourceArn",
    },
    closed=True,
)


class _ActionGroupExecutor_customControl(TypedDict, closed=True):
    customControl: (
        "capo_bedrock_agent_runtime.types.custom_control_method.CustomControlMethod"
    )


ActionGroupExecutor: TypeAlias = (
    _ActionGroupExecutor_lambda | _ActionGroupExecutor_customControl
)


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupExecutor) -> dict:
    if "lambda" in value:
        return {"lambda": value["lambda"]}
    elif "customControl" in value:
        import capo_bedrock_agent_runtime.types.custom_control_method

        return {
            "customControl": capo_bedrock_agent_runtime.types.custom_control_method.serialize_json(
                value["customControl"]
            )
        }
    else:
        raise SerializationError("ActionGroupExecutor: no variant present")


def deserialize_json(data: dict) -> ActionGroupExecutor:
    if "lambda" in data:
        return {"lambda": data["lambda"]}
    elif "customControl" in data:
        import capo_bedrock_agent_runtime.types.custom_control_method

        return {
            "customControl": capo_bedrock_agent_runtime.types.custom_control_method.deserialize_json(
                data["customControl"]
            )
        }
    else:
        raise DeserializationError("ActionGroupExecutor: no recognized variant key")
