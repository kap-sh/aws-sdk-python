"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.arn
    import capo_service_catalog_appregistry.types.resource_group_state
    import capo_service_catalog_appregistry.types.string


class ResourceGroup(TypedDict, closed=True):
    state: NotRequired[
        "capo_service_catalog_appregistry.types.resource_group_state.ResourceGroupState"
    ]
    """<p>The state of the propagation process for the resource group. The states includes:</p> <p> <code>CREATING </code>if the resource group is in the process of being created.</p> <p> <code>CREATE_COMPLETE</code> if the resource group was created successfully.</p> <p> <code>CREATE_FAILED</code> if the resource group failed to be created.</p> <p> <code>UPDATING</code> if the resource group is in the process of being updated.</p> <p> <code>UPDATE_COMPLETE</code> if the resource group updated successfully.</p> <p> <code>UPDATE_FAILED</code> if the resource group could not update successfully.</p>"""
    arn: NotRequired["capo_service_catalog_appregistry.types.arn.Arn"]
    """<p>The Amazon resource name (ARN) of the resource group.</p>"""
    error_message: NotRequired["capo_service_catalog_appregistry.types.string.String"]
    """<p>The error message that generates when the propagation process for the resource group fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGroup) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_service_catalog_appregistry.types.resource_group_state

        out["state"] = (
            capo_service_catalog_appregistry.types.resource_group_state.serialize_json(
                value["state"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ResourceGroup:
    out: ResourceGroup = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_service_catalog_appregistry.types.resource_group_state

        out["state"] = (
            capo_service_catalog_appregistry.types.resource_group_state.deserialize_json(
                data["state"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
