"""Generated from Smithy shape ``com.amazonaws.greengrass#GetResourceDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetResourceDefinitionRequest(TypedDict, closed=True):
    resource_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the resource definition."""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceDefinitionRequest:
    out: GetResourceDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
