"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginAuthConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.basic_auth_configuration
    import capo_qbusiness.types.idc_auth_configuration
    import capo_qbusiness.types.no_auth_configuration
    import capo_qbusiness.types.o_auth2_client_credential_configuration


class _PluginAuthConfiguration_basicAuthConfiguration(TypedDict, closed=True):
    basicAuthConfiguration: (
        "capo_qbusiness.types.basic_auth_configuration.BasicAuthConfiguration"
    )


class _PluginAuthConfiguration_oAuth2ClientCredentialConfiguration(
    TypedDict, closed=True
):
    oAuth2ClientCredentialConfiguration: "capo_qbusiness.types.o_auth2_client_credential_configuration.OAuth2ClientCredentialConfiguration"


class _PluginAuthConfiguration_noAuthConfiguration(TypedDict, closed=True):
    noAuthConfiguration: (
        "capo_qbusiness.types.no_auth_configuration.NoAuthConfiguration"
    )


class _PluginAuthConfiguration_idcAuthConfiguration(TypedDict, closed=True):
    idcAuthConfiguration: (
        "capo_qbusiness.types.idc_auth_configuration.IdcAuthConfiguration"
    )


PluginAuthConfiguration: TypeAlias = (
    _PluginAuthConfiguration_basicAuthConfiguration
    | _PluginAuthConfiguration_oAuth2ClientCredentialConfiguration
    | _PluginAuthConfiguration_noAuthConfiguration
    | _PluginAuthConfiguration_idcAuthConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: PluginAuthConfiguration) -> dict:
    if "basicAuthConfiguration" in value:
        import capo_qbusiness.types.basic_auth_configuration

        return {
            "basicAuthConfiguration": capo_qbusiness.types.basic_auth_configuration.serialize_json(
                value["basicAuthConfiguration"]
            )
        }
    elif "oAuth2ClientCredentialConfiguration" in value:
        import capo_qbusiness.types.o_auth2_client_credential_configuration

        return {
            "oAuth2ClientCredentialConfiguration": capo_qbusiness.types.o_auth2_client_credential_configuration.serialize_json(
                value["oAuth2ClientCredentialConfiguration"]
            )
        }
    elif "noAuthConfiguration" in value:
        import capo_qbusiness.types.no_auth_configuration

        return {
            "noAuthConfiguration": capo_qbusiness.types.no_auth_configuration.serialize_json(
                value["noAuthConfiguration"]
            )
        }
    elif "idcAuthConfiguration" in value:
        import capo_qbusiness.types.idc_auth_configuration

        return {
            "idcAuthConfiguration": capo_qbusiness.types.idc_auth_configuration.serialize_json(
                value["idcAuthConfiguration"]
            )
        }
    else:
        raise SerializationError("PluginAuthConfiguration: no variant present")


def deserialize_json(data: dict) -> PluginAuthConfiguration:
    if "basicAuthConfiguration" in data:
        import capo_qbusiness.types.basic_auth_configuration

        return {
            "basicAuthConfiguration": capo_qbusiness.types.basic_auth_configuration.deserialize_json(
                data["basicAuthConfiguration"]
            )
        }
    elif "oAuth2ClientCredentialConfiguration" in data:
        import capo_qbusiness.types.o_auth2_client_credential_configuration

        return {
            "oAuth2ClientCredentialConfiguration": capo_qbusiness.types.o_auth2_client_credential_configuration.deserialize_json(
                data["oAuth2ClientCredentialConfiguration"]
            )
        }
    elif "noAuthConfiguration" in data:
        import capo_qbusiness.types.no_auth_configuration

        return {
            "noAuthConfiguration": capo_qbusiness.types.no_auth_configuration.deserialize_json(
                data["noAuthConfiguration"]
            )
        }
    elif "idcAuthConfiguration" in data:
        import capo_qbusiness.types.idc_auth_configuration

        return {
            "idcAuthConfiguration": capo_qbusiness.types.idc_auth_configuration.deserialize_json(
                data["idcAuthConfiguration"]
            )
        }
    else:
        raise DeserializationError("PluginAuthConfiguration: no recognized variant key")
