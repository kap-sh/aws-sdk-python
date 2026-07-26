"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateFunctionDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class UpdateFunctionDefinitionRequest(TypedDict, closed=True):
    function_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the Lambda function definition."""
    name: NotRequired["capo_greengrass.types.__string.__string"]
    """The name of the definition."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFunctionDefinitionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateFunctionDefinitionRequest:
    out: UpdateFunctionDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
