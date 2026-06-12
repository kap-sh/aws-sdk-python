"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#PutConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.app_registry_configuration


class PutConfigurationRequest(TypedDict):
    configuration: "aws_sdk_service_catalog_appregistry.types.app_registry_configuration.AppRegistryConfiguration"
    """<p> Associates a <code>TagKey</code> configuration to an account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_service_catalog_appregistry.types.app_registry_configuration

    out["configuration"] = (
        aws_sdk_service_catalog_appregistry.types.app_registry_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutConfigurationRequest:
    out: PutConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_service_catalog_appregistry.types.app_registry_configuration

        out["configuration"] = (
            aws_sdk_service_catalog_appregistry.types.app_registry_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("PutConfigurationRequest.configuration required")
    return out
