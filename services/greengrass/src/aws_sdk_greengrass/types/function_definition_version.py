"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionDefinitionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_function
    import aws_sdk_greengrass.types.function_default_config


class FunctionDefinitionVersion(TypedDict, closed=True):
    default_config: NotRequired[
        "aws_sdk_greengrass.types.function_default_config.FunctionDefaultConfig"
    ]
    """The default configuration that applies to all Lambda functions in this function definition version. Individual Lambda functions can override these settings."""
    functions: NotRequired[
        "aws_sdk_greengrass.types.__list_of_function.__listOfFunction"
    ]
    """A list of Lambda functions in this function definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionDefinitionVersion) -> dict:
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


def deserialize_json(data: dict) -> FunctionDefinitionVersion:
    out: FunctionDefinitionVersion = {}  # type: ignore[typeddict-item]
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
