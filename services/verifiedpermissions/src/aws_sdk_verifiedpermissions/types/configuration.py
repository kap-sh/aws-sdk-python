"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration
    import aws_sdk_verifiedpermissions.types.open_id_connect_configuration

class _Configuration_cognitoUserPoolConfiguration(TypedDict):
    cognitoUserPoolConfiguration: "aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration.CognitoUserPoolConfiguration"


class _Configuration_openIdConnectConfiguration(TypedDict):
    openIdConnectConfiguration: "aws_sdk_verifiedpermissions.types.open_id_connect_configuration.OpenIdConnectConfiguration"

Configuration: TypeAlias = _Configuration_cognitoUserPoolConfiguration | _Configuration_openIdConnectConfiguration

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Configuration) -> dict:
    if "cognitoUserPoolConfiguration" in value:
        import aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration
        return {"cognitoUserPoolConfiguration": aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration.serialize_aws_json_1_0(value["cognitoUserPoolConfiguration"])}
    elif "openIdConnectConfiguration" in value:
        import aws_sdk_verifiedpermissions.types.open_id_connect_configuration
        return {"openIdConnectConfiguration": aws_sdk_verifiedpermissions.types.open_id_connect_configuration.serialize_aws_json_1_0(value["openIdConnectConfiguration"])}
    else:
        raise SerializationError("Configuration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Configuration:
    if "cognitoUserPoolConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration
        return {"cognitoUserPoolConfiguration": aws_sdk_verifiedpermissions.types.cognito_user_pool_configuration.deserialize_aws_json_1_0(data["cognitoUserPoolConfiguration"])}
    elif "openIdConnectConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_configuration
        return {"openIdConnectConfiguration": aws_sdk_verifiedpermissions.types.open_id_connect_configuration.deserialize_aws_json_1_0(data["openIdConnectConfiguration"])}
    else:
        raise DeserializationError("Configuration: no recognized variant key")