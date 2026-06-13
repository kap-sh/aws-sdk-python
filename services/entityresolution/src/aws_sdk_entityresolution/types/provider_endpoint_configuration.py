"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderEndpointConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.provider_marketplace_configuration


class _ProviderEndpointConfiguration_marketplaceConfiguration(TypedDict):
    marketplaceConfiguration: "aws_sdk_entityresolution.types.provider_marketplace_configuration.ProviderMarketplaceConfiguration"


ProviderEndpointConfiguration: TypeAlias = (
    _ProviderEndpointConfiguration_marketplaceConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderEndpointConfiguration) -> dict:
    if "marketplaceConfiguration" in value:
        import aws_sdk_entityresolution.types.provider_marketplace_configuration

        return {
            "marketplaceConfiguration": aws_sdk_entityresolution.types.provider_marketplace_configuration.serialize_json(
                value["marketplaceConfiguration"]
            )
        }
    else:
        raise SerializationError("ProviderEndpointConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderEndpointConfiguration:
    if "marketplaceConfiguration" in data:
        import aws_sdk_entityresolution.types.provider_marketplace_configuration

        return {
            "marketplaceConfiguration": aws_sdk_entityresolution.types.provider_marketplace_configuration.deserialize_json(
                data["marketplaceConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ProviderEndpointConfiguration: no recognized variant key"
        )
