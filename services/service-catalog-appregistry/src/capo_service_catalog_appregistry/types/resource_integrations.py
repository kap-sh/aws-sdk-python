"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceIntegrations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.resource_group


class ResourceIntegrations(TypedDict, closed=True):
    resource_group: NotRequired[
        "capo_service_catalog_appregistry.types.resource_group.ResourceGroup"
    ]
    """<p>The information about the integration of Resource Groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIntegrations) -> dict:
    out: dict = {}
    if "resource_group" in value:
        import capo_service_catalog_appregistry.types.resource_group

        out["resourceGroup"] = (
            capo_service_catalog_appregistry.types.resource_group.serialize_json(
                value["resource_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceIntegrations:
    out: ResourceIntegrations = {}  # type: ignore[typeddict-item]
    if "resourceGroup" in data:
        import capo_service_catalog_appregistry.types.resource_group

        out["resource_group"] = (
            capo_service_catalog_appregistry.types.resource_group.deserialize_json(
                data["resourceGroup"]
            )
        )
    return out
