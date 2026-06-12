"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.app_registry_configuration


class GetConfigurationResponse(TypedDict):
    configuration: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.app_registry_configuration.AppRegistryConfiguration"
    ]
    """<p> Retrieves <code>TagKey</code> configuration from an account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_service_catalog_appregistry.types.app_registry_configuration

        out["configuration"] = (
            aws_sdk_service_catalog_appregistry.types.app_registry_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationResponse:
    out: GetConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_service_catalog_appregistry.types.app_registry_configuration

        out["configuration"] = (
            aws_sdk_service_catalog_appregistry.types.app_registry_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
