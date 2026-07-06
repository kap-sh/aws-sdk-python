"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateOpenIdConnectTokenSelection``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.update_open_id_connect_access_token_configuration
    import aws_sdk_verifiedpermissions.types.update_open_id_connect_identity_token_configuration


class _UpdateOpenIdConnectTokenSelection_accessTokenOnly(TypedDict, closed=True):
    accessTokenOnly: "aws_sdk_verifiedpermissions.types.update_open_id_connect_access_token_configuration.UpdateOpenIdConnectAccessTokenConfiguration"


class _UpdateOpenIdConnectTokenSelection_identityTokenOnly(TypedDict, closed=True):
    identityTokenOnly: "aws_sdk_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.UpdateOpenIdConnectIdentityTokenConfiguration"


UpdateOpenIdConnectTokenSelection: TypeAlias = (
    _UpdateOpenIdConnectTokenSelection_accessTokenOnly
    | _UpdateOpenIdConnectTokenSelection_identityTokenOnly
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOpenIdConnectTokenSelection) -> dict:
    if "accessTokenOnly" in value:
        import aws_sdk_verifiedpermissions.types.update_open_id_connect_access_token_configuration

        return {
            "accessTokenOnly": aws_sdk_verifiedpermissions.types.update_open_id_connect_access_token_configuration.serialize_aws_json_1_0(
                value["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in value:
        import aws_sdk_verifiedpermissions.types.update_open_id_connect_identity_token_configuration

        return {
            "identityTokenOnly": aws_sdk_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.serialize_aws_json_1_0(
                value["identityTokenOnly"]
            )
        }
    else:
        raise SerializationError(
            "UpdateOpenIdConnectTokenSelection: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> UpdateOpenIdConnectTokenSelection:
    if "accessTokenOnly" in data:
        import aws_sdk_verifiedpermissions.types.update_open_id_connect_access_token_configuration

        return {
            "accessTokenOnly": aws_sdk_verifiedpermissions.types.update_open_id_connect_access_token_configuration.deserialize_aws_json_1_0(
                data["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in data:
        import aws_sdk_verifiedpermissions.types.update_open_id_connect_identity_token_configuration

        return {
            "identityTokenOnly": aws_sdk_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.deserialize_aws_json_1_0(
                data["identityTokenOnly"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateOpenIdConnectTokenSelection: no recognized variant key"
        )
