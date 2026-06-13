"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginAuthConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.basic_auth_configuration
    import aws_sdk_qbusiness.types.idc_auth_configuration
    import aws_sdk_qbusiness.types.no_auth_configuration
    import aws_sdk_qbusiness.types.o_auth2_client_credential_configuration


class _PluginAuthConfiguration_basicAuthConfiguration(TypedDict):
    basicAuthConfiguration: (
        "aws_sdk_qbusiness.types.basic_auth_configuration.BasicAuthConfiguration"
    )


class _PluginAuthConfiguration_oAuth2ClientCredentialConfiguration(TypedDict):
    oAuth2ClientCredentialConfiguration: "aws_sdk_qbusiness.types.o_auth2_client_credential_configuration.OAuth2ClientCredentialConfiguration"


class _PluginAuthConfiguration_noAuthConfiguration(TypedDict):
    noAuthConfiguration: (
        "aws_sdk_qbusiness.types.no_auth_configuration.NoAuthConfiguration"
    )


class _PluginAuthConfiguration_idcAuthConfiguration(TypedDict):
    idcAuthConfiguration: (
        "aws_sdk_qbusiness.types.idc_auth_configuration.IdcAuthConfiguration"
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
        import aws_sdk_qbusiness.types.basic_auth_configuration

        return {
            "basicAuthConfiguration": aws_sdk_qbusiness.types.basic_auth_configuration.serialize_json(
                value["basicAuthConfiguration"]
            )
        }
    elif "oAuth2ClientCredentialConfiguration" in value:
        import aws_sdk_qbusiness.types.o_auth2_client_credential_configuration

        return {
            "oAuth2ClientCredentialConfiguration": aws_sdk_qbusiness.types.o_auth2_client_credential_configuration.serialize_json(
                value["oAuth2ClientCredentialConfiguration"]
            )
        }
    elif "noAuthConfiguration" in value:
        import aws_sdk_qbusiness.types.no_auth_configuration

        return {
            "noAuthConfiguration": aws_sdk_qbusiness.types.no_auth_configuration.serialize_json(
                value["noAuthConfiguration"]
            )
        }
    elif "idcAuthConfiguration" in value:
        import aws_sdk_qbusiness.types.idc_auth_configuration

        return {
            "idcAuthConfiguration": aws_sdk_qbusiness.types.idc_auth_configuration.serialize_json(
                value["idcAuthConfiguration"]
            )
        }
    else:
        raise SerializationError("PluginAuthConfiguration: no variant present")


def deserialize_json(data: dict) -> PluginAuthConfiguration:
    if "basicAuthConfiguration" in data:
        import aws_sdk_qbusiness.types.basic_auth_configuration

        return {
            "basicAuthConfiguration": aws_sdk_qbusiness.types.basic_auth_configuration.deserialize_json(
                data["basicAuthConfiguration"]
            )
        }
    elif "oAuth2ClientCredentialConfiguration" in data:
        import aws_sdk_qbusiness.types.o_auth2_client_credential_configuration

        return {
            "oAuth2ClientCredentialConfiguration": aws_sdk_qbusiness.types.o_auth2_client_credential_configuration.deserialize_json(
                data["oAuth2ClientCredentialConfiguration"]
            )
        }
    elif "noAuthConfiguration" in data:
        import aws_sdk_qbusiness.types.no_auth_configuration

        return {
            "noAuthConfiguration": aws_sdk_qbusiness.types.no_auth_configuration.deserialize_json(
                data["noAuthConfiguration"]
            )
        }
    elif "idcAuthConfiguration" in data:
        import aws_sdk_qbusiness.types.idc_auth_configuration

        return {
            "idcAuthConfiguration": aws_sdk_qbusiness.types.idc_auth_configuration.deserialize_json(
                data["idcAuthConfiguration"]
            )
        }
    else:
        raise DeserializationError("PluginAuthConfiguration: no recognized variant key")
