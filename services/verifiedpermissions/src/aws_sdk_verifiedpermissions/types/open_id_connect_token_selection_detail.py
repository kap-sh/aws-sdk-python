"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectTokenSelectionDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_detail
    import aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail


class _OpenIdConnectTokenSelectionDetail_accessTokenOnly(TypedDict, closed=True):
    accessTokenOnly: "aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_detail.OpenIdConnectAccessTokenConfigurationDetail"


class _OpenIdConnectTokenSelectionDetail_identityTokenOnly(TypedDict, closed=True):
    identityTokenOnly: "aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail.OpenIdConnectIdentityTokenConfigurationDetail"


OpenIdConnectTokenSelectionDetail: TypeAlias = (
    _OpenIdConnectTokenSelectionDetail_accessTokenOnly
    | _OpenIdConnectTokenSelectionDetail_identityTokenOnly
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectTokenSelectionDetail) -> dict:
    if "accessTokenOnly" in value:
        import aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_detail

        return {
            "accessTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_detail.serialize_aws_json_1_0(
                value["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in value:
        import aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail

        return {
            "identityTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail.serialize_aws_json_1_0(
                value["identityTokenOnly"]
            )
        }
    else:
        raise SerializationError(
            "OpenIdConnectTokenSelectionDetail: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectTokenSelectionDetail:
    if "accessTokenOnly" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_detail

        return {
            "accessTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_access_token_configuration_detail.deserialize_aws_json_1_0(
                data["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail

        return {
            "identityTokenOnly": aws_sdk_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail.deserialize_aws_json_1_0(
                data["identityTokenOnly"]
            )
        }
    else:
        raise DeserializationError(
            "OpenIdConnectTokenSelectionDetail: no recognized variant key"
        )
