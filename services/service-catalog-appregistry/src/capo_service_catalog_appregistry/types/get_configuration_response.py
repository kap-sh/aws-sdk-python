"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.app_registry_configuration


class GetConfigurationResponse(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_service_catalog_appregistry.types.app_registry_configuration.AppRegistryConfiguration"
    ]
    """<p> Retrieves <code>TagKey</code> configuration from an account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_service_catalog_appregistry.types.app_registry_configuration

        out["configuration"] = (
            capo_service_catalog_appregistry.types.app_registry_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationResponse:
    out: GetConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_service_catalog_appregistry.types.app_registry_configuration

        out["configuration"] = (
            capo_service_catalog_appregistry.types.app_registry_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
