"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteCoreDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class DeleteCoreDefinitionRequest(TypedDict, closed=True):
    core_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the core definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCoreDefinitionRequest:
    out: DeleteCoreDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
