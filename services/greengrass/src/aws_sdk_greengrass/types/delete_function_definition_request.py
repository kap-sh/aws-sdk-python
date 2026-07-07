"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteFunctionDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class DeleteFunctionDefinitionRequest(TypedDict, closed=True):
    function_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Lambda function definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionDefinitionRequest:
    out: DeleteFunctionDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
