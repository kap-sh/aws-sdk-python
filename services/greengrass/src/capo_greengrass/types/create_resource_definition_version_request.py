"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateResourceDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_resource
    import capo_greengrass.types.__string


class CreateResourceDefinitionVersionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    resource_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the resource definition."""
    resources: NotRequired["capo_greengrass.types.__list_of_resource.__listOfResource"]
    """A list of resources."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_greengrass.types.__list_of_resource

        out["Resources"] = capo_greengrass.types.__list_of_resource.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> CreateResourceDefinitionVersionRequest:
    out: CreateResourceDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import capo_greengrass.types.__list_of_resource

        out["resources"] = capo_greengrass.types.__list_of_resource.deserialize_json(
            data["Resources"]
        )
    return out
