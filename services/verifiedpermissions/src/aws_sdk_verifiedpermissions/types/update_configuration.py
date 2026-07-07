"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.update_cognito_user_pool_configuration
    import aws_sdk_verifiedpermissions.types.update_open_id_connect_configuration


class _UpdateConfiguration_cognitoUserPoolConfiguration(TypedDict, closed=True):
    cognitoUserPoolConfiguration: "aws_sdk_verifiedpermissions.types.update_cognito_user_pool_configuration.UpdateCognitoUserPoolConfiguration"


class _UpdateConfiguration_openIdConnectConfiguration(TypedDict, closed=True):
    openIdConnectConfiguration: "aws_sdk_verifiedpermissions.types.update_open_id_connect_configuration.UpdateOpenIdConnectConfiguration"


UpdateConfiguration: TypeAlias = (
    _UpdateConfiguration_cognitoUserPoolConfiguration
    | _UpdateConfiguration_openIdConnectConfiguration
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateConfiguration) -> dict:
    if "cognitoUserPoolConfiguration" in value:
        import aws_sdk_verifiedpermissions.types.update_cognito_user_pool_configuration

        return {
            "cognitoUserPoolConfiguration": aws_sdk_verifiedpermissions.types.update_cognito_user_pool_configuration.serialize_aws_json_1_0(
                value["cognitoUserPoolConfiguration"]
            )
        }
    elif "openIdConnectConfiguration" in value:
        import aws_sdk_verifiedpermissions.types.update_open_id_connect_configuration

        return {
            "openIdConnectConfiguration": aws_sdk_verifiedpermissions.types.update_open_id_connect_configuration.serialize_aws_json_1_0(
                value["openIdConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("UpdateConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> UpdateConfiguration:
    if "cognitoUserPoolConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.update_cognito_user_pool_configuration

        return {
            "cognitoUserPoolConfiguration": aws_sdk_verifiedpermissions.types.update_cognito_user_pool_configuration.deserialize_aws_json_1_0(
                data["cognitoUserPoolConfiguration"]
            )
        }
    elif "openIdConnectConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.update_open_id_connect_configuration

        return {
            "openIdConnectConfiguration": aws_sdk_verifiedpermissions.types.update_open_id_connect_configuration.deserialize_aws_json_1_0(
                data["openIdConnectConfiguration"]
            )
        }
    else:
        raise DeserializationError("UpdateConfiguration: no recognized variant key")
