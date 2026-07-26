"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteResourceDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class DeleteResourceDefinitionRequest(TypedDict, closed=True):
    resource_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the resource definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourceDefinitionRequest:
    out: DeleteResourceDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
