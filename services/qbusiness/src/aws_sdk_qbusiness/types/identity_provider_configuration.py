"""Generated from Smithy shape ``com.amazonaws.qbusiness#IdentityProviderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.open_id_connect_provider_configuration
    import aws_sdk_qbusiness.types.saml_provider_configuration


class _IdentityProviderConfiguration_samlConfiguration(TypedDict):
    samlConfiguration: (
        "aws_sdk_qbusiness.types.saml_provider_configuration.SamlProviderConfiguration"
    )


class _IdentityProviderConfiguration_openIDConnectConfiguration(TypedDict):
    openIDConnectConfiguration: "aws_sdk_qbusiness.types.open_id_connect_provider_configuration.OpenIDConnectProviderConfiguration"


IdentityProviderConfiguration: TypeAlias = (
    _IdentityProviderConfiguration_samlConfiguration
    | _IdentityProviderConfiguration_openIDConnectConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderConfiguration) -> dict:
    if "samlConfiguration" in value:
        import aws_sdk_qbusiness.types.saml_provider_configuration

        return {
            "samlConfiguration": aws_sdk_qbusiness.types.saml_provider_configuration.serialize_json(
                value["samlConfiguration"]
            )
        }
    elif "openIDConnectConfiguration" in value:
        import aws_sdk_qbusiness.types.open_id_connect_provider_configuration

        return {
            "openIDConnectConfiguration": aws_sdk_qbusiness.types.open_id_connect_provider_configuration.serialize_json(
                value["openIDConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("IdentityProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> IdentityProviderConfiguration:
    if "samlConfiguration" in data:
        import aws_sdk_qbusiness.types.saml_provider_configuration

        return {
            "samlConfiguration": aws_sdk_qbusiness.types.saml_provider_configuration.deserialize_json(
                data["samlConfiguration"]
            )
        }
    elif "openIDConnectConfiguration" in data:
        import aws_sdk_qbusiness.types.open_id_connect_provider_configuration

        return {
            "openIDConnectConfiguration": aws_sdk_qbusiness.types.open_id_connect_provider_configuration.deserialize_json(
                data["openIDConnectConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "IdentityProviderConfiguration: no recognized variant key"
        )
