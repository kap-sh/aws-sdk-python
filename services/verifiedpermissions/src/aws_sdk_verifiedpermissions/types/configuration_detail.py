"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ConfigurationDetail``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration_detail
    import aws_sdk_verifiedpermissions.types.open_id_connect_configuration_detail


class _ConfigurationDetail_cognitoUserPoolConfiguration(TypedDict):
    cognitoUserPoolConfiguration: "aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration_detail.CognitoUserPoolConfigurationDetail"


class _ConfigurationDetail_openIdConnectConfiguration(TypedDict):
    openIdConnectConfiguration: "aws_sdk_verifiedpermissions.types.open_id_connect_configuration_detail.OpenIdConnectConfigurationDetail"


ConfigurationDetail: TypeAlias = (
    _ConfigurationDetail_cognitoUserPoolConfiguration
    | _ConfigurationDetail_openIdConnectConfiguration
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationDetail) -> dict:
    if "cognitoUserPoolConfiguration" in value:
        import aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration_detail

        return {
            "cognitoUserPoolConfiguration": aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration_detail.serialize_aws_json_1_0(
                value["cognitoUserPoolConfiguration"]
            )
        }
    elif "openIdConnectConfiguration" in value:
        import aws_sdk_verifiedpermissions.types.open_id_connect_configuration_detail

        return {
            "openIdConnectConfiguration": aws_sdk_verifiedpermissions.types.open_id_connect_configuration_detail.serialize_aws_json_1_0(
                value["openIdConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("ConfigurationDetail: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ConfigurationDetail:
    if "cognitoUserPoolConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration_detail

        return {
            "cognitoUserPoolConfiguration": aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration_detail.deserialize_aws_json_1_0(
                data["cognitoUserPoolConfiguration"]
            )
        }
    elif "openIdConnectConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_configuration_detail

        return {
            "openIdConnectConfiguration": aws_sdk_verifiedpermissions.types.open_id_connect_configuration_detail.deserialize_aws_json_1_0(
                data["openIdConnectConfiguration"]
            )
        }
    else:
        raise DeserializationError("ConfigurationDetail: no recognized variant key")
