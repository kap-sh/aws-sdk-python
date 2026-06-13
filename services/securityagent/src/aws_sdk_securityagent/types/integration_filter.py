"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegrationFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.provider
    import aws_sdk_securityagent.types.provider_type


class _IntegrationFilter_provider(TypedDict):
    provider: "aws_sdk_securityagent.types.provider.Provider"


class _IntegrationFilter_providerType(TypedDict):
    providerType: "aws_sdk_securityagent.types.provider_type.ProviderType"


IntegrationFilter: TypeAlias = (
    _IntegrationFilter_provider | _IntegrationFilter_providerType
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationFilter) -> dict:
    if "provider" in value:
        import aws_sdk_securityagent.types.provider

        return {
            "provider": aws_sdk_securityagent.types.provider.serialize_json(
                value["provider"]
            )
        }
    elif "providerType" in value:
        import aws_sdk_securityagent.types.provider_type

        return {
            "providerType": aws_sdk_securityagent.types.provider_type.serialize_json(
                value["providerType"]
            )
        }
    else:
        raise SerializationError("IntegrationFilter: no variant present")


def deserialize_json(data: dict) -> IntegrationFilter:
    if "provider" in data:
        import aws_sdk_securityagent.types.provider

        return {
            "provider": aws_sdk_securityagent.types.provider.deserialize_json(
                data["provider"]
            )
        }
    elif "providerType" in data:
        import aws_sdk_securityagent.types.provider_type

        return {
            "providerType": aws_sdk_securityagent.types.provider_type.deserialize_json(
                data["providerType"]
            )
        }
    else:
        raise DeserializationError("IntegrationFilter: no recognized variant key")
