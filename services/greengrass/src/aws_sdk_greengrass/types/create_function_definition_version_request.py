"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateFunctionDefinitionVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_function
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.function_default_config


class CreateFunctionDefinitionVersionRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    default_config: NotRequired[
        "aws_sdk_greengrass.types.function_default_config.FunctionDefaultConfig"
    ]
    """The default configuration that applies to all Lambda functions in this function definition version. Individual Lambda functions can override these settings."""
    function_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Lambda function definition."""
    functions: NotRequired[
        "aws_sdk_greengrass.types.__list_of_function.__listOfFunction"
    ]
    """A list of Lambda functions in this function definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFunctionDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "default_config" in value:
        import aws_sdk_greengrass.types.function_default_config

        out["DefaultConfig"] = (
            aws_sdk_greengrass.types.function_default_config.serialize_json(
                value["default_config"]
            )
        )
    if "functions" in value:
        import aws_sdk_greengrass.types.__list_of_function

        out["Functions"] = aws_sdk_greengrass.types.__list_of_function.serialize_json(
            value["functions"]
        )
    return out


def deserialize_json(data: dict) -> CreateFunctionDefinitionVersionRequest:
    out: CreateFunctionDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "DefaultConfig" in data:
        import aws_sdk_greengrass.types.function_default_config

        out["default_config"] = (
            aws_sdk_greengrass.types.function_default_config.deserialize_json(
                data["DefaultConfig"]
            )
        )
    if "Functions" in data:
        import aws_sdk_greengrass.types.__list_of_function

        out["functions"] = aws_sdk_greengrass.types.__list_of_function.deserialize_json(
            data["Functions"]
        )
    return out
