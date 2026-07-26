"""Generated from Smithy shape ``com.amazonaws.greengrass#Function``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.function_configuration


class Function(TypedDict, closed=True):
    function_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the Lambda function."""
    function_configuration: NotRequired[
        "capo_greengrass.types.function_configuration.FunctionConfiguration"
    ]
    """The configuration of the Lambda function."""
    id: NotRequired["capo_greengrass.types.__string.__string"]
    """A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''."""


# --- restJson1 ser/de ---
def serialize_json(value: Function) -> dict:
    out: dict = {}
    if "function_arn" in value:
        out["FunctionArn"] = value["function_arn"]
    if "function_configuration" in value:
        import capo_greengrass.types.function_configuration

        out["FunctionConfiguration"] = (
            capo_greengrass.types.function_configuration.serialize_json(
                value["function_configuration"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> Function:
    out: Function = {}  # type: ignore[typeddict-item]
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    if "FunctionConfiguration" in data:
        import capo_greengrass.types.function_configuration

        out["function_configuration"] = (
            capo_greengrass.types.function_configuration.deserialize_json(
                data["FunctionConfiguration"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    return out
