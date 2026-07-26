"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegrationFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.provider
    import capo_securityagent.types.provider_type


class _IntegrationFilter_provider(TypedDict, closed=True):
    provider: "capo_securityagent.types.provider.Provider"


class _IntegrationFilter_providerType(TypedDict, closed=True):
    providerType: "capo_securityagent.types.provider_type.ProviderType"


IntegrationFilter: TypeAlias = (
    _IntegrationFilter_provider | _IntegrationFilter_providerType
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationFilter) -> dict:
    if "provider" in value:
        import capo_securityagent.types.provider

        return {
            "provider": capo_securityagent.types.provider.serialize_json(
                value["provider"]
            )
        }
    elif "providerType" in value:
        import capo_securityagent.types.provider_type

        return {
            "providerType": capo_securityagent.types.provider_type.serialize_json(
                value["providerType"]
            )
        }
    else:
        raise SerializationError("IntegrationFilter: no variant present")


def deserialize_json(data: dict) -> IntegrationFilter:
    if "provider" in data:
        import capo_securityagent.types.provider

        return {
            "provider": capo_securityagent.types.provider.deserialize_json(
                data["provider"]
            )
        }
    elif "providerType" in data:
        import capo_securityagent.types.provider_type

        return {
            "providerType": capo_securityagent.types.provider_type.deserialize_json(
                data["providerType"]
            )
        }
    else:
        raise DeserializationError("IntegrationFilter: no recognized variant key")
