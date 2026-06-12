"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateResourceDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class UpdateResourceDefinitionRequest(TypedDict):
    name: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the definition."""
    resource_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the resource definition."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceDefinitionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateResourceDefinitionRequest:
    out: UpdateResourceDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
