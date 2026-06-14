"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectTokenSelectionItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_item
    import aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_item


class _OpenIdConnectTokenSelectionItem_accessTokenOnly(TypedDict):
    accessTokenOnly: "aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_item.OpenIdConnectAccessTokenConfigurationItem"


class _OpenIdConnectTokenSelectionItem_identityTokenOnly(TypedDict):
    identityTokenOnly: "aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_item.OpenIdConnectIdentityTokenConfigurationItem"


OpenIdConnectTokenSelectionItem: TypeAlias = (
    _OpenIdConnectTokenSelectionItem_accessTokenOnly
    | _OpenIdConnectTokenSelectionItem_identityTokenOnly
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectTokenSelectionItem) -> dict:
    if "accessTokenOnly" in value:
        import aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_item

        return {
            "accessTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_item.serialize_aws_json_1_0(
                value["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in value:
        import aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_item

        return {
            "identityTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_item.serialize_aws_json_1_0(
                value["identityTokenOnly"]
            )
        }
    else:
        raise SerializationError("OpenIdConnectTokenSelectionItem: no variant present")


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectTokenSelectionItem:
    if "accessTokenOnly" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_item

        return {
            "accessTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_item.deserialize_aws_json_1_0(
                data["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_item

        return {
            "identityTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_item.deserialize_aws_json_1_0(
                data["identityTokenOnly"]
            )
        }
    else:
        raise DeserializationError(
            "OpenIdConnectTokenSelectionItem: no recognized variant key"
        )
