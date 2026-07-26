"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderEndpointConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.provider_marketplace_configuration


class _ProviderEndpointConfiguration_marketplaceConfiguration(TypedDict, closed=True):
    marketplaceConfiguration: "capo_entityresolution.types.provider_marketplace_configuration.ProviderMarketplaceConfiguration"


ProviderEndpointConfiguration: TypeAlias = (
    _ProviderEndpointConfiguration_marketplaceConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderEndpointConfiguration) -> dict:
    if "marketplaceConfiguration" in value:
        import capo_entityresolution.types.provider_marketplace_configuration

        return {
            "marketplaceConfiguration": capo_entityresolution.types.provider_marketplace_configuration.serialize_json(
                value["marketplaceConfiguration"]
            )
        }
    else:
        raise SerializationError("ProviderEndpointConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderEndpointConfiguration:
    if "marketplaceConfiguration" in data:
        import capo_entityresolution.types.provider_marketplace_configuration

        return {
            "marketplaceConfiguration": capo_entityresolution.types.provider_marketplace_configuration.deserialize_json(
                data["marketplaceConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ProviderEndpointConfiguration: no recognized variant key"
        )
