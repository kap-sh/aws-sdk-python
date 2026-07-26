"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#PutConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_service_catalog_appregistry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.app_registry_configuration


class PutConfigurationRequest(TypedDict, closed=True):
    configuration: "capo_service_catalog_appregistry.types.app_registry_configuration.AppRegistryConfiguration"
    """<p> Associates a <code>TagKey</code> configuration to an account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationRequest) -> dict:
    out: dict = {}
    import capo_service_catalog_appregistry.types.app_registry_configuration

    out["configuration"] = (
        capo_service_catalog_appregistry.types.app_registry_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutConfigurationRequest:
    out: PutConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_service_catalog_appregistry.types.app_registry_configuration

        out["configuration"] = (
            capo_service_catalog_appregistry.types.app_registry_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("PutConfigurationRequest.configuration required")
    return out
