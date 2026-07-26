"""Generated from Smithy shape ``com.amazonaws.qbusiness#IdentityProviderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.open_id_connect_provider_configuration
    import capo_qbusiness.types.saml_provider_configuration


class _IdentityProviderConfiguration_samlConfiguration(TypedDict, closed=True):
    samlConfiguration: (
        "capo_qbusiness.types.saml_provider_configuration.SamlProviderConfiguration"
    )


class _IdentityProviderConfiguration_openIDConnectConfiguration(TypedDict, closed=True):
    openIDConnectConfiguration: "capo_qbusiness.types.open_id_connect_provider_configuration.OpenIDConnectProviderConfiguration"


IdentityProviderConfiguration: TypeAlias = (
    _IdentityProviderConfiguration_samlConfiguration
    | _IdentityProviderConfiguration_openIDConnectConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderConfiguration) -> dict:
    if "samlConfiguration" in value:
        import capo_qbusiness.types.saml_provider_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_provider_configuration.serialize_json(
                value["samlConfiguration"]
            )
        }
    elif "openIDConnectConfiguration" in value:
        import capo_qbusiness.types.open_id_connect_provider_configuration

        return {
            "openIDConnectConfiguration": capo_qbusiness.types.open_id_connect_provider_configuration.serialize_json(
                value["openIDConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("IdentityProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> IdentityProviderConfiguration:
    if "samlConfiguration" in data:
        import capo_qbusiness.types.saml_provider_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_provider_configuration.deserialize_json(
                data["samlConfiguration"]
            )
        }
    elif "openIDConnectConfiguration" in data:
        import capo_qbusiness.types.open_id_connect_provider_configuration

        return {
            "openIDConnectConfiguration": capo_qbusiness.types.open_id_connect_provider_configuration.deserialize_json(
                data["openIDConnectConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "IdentityProviderConfiguration: no recognized variant key"
        )
