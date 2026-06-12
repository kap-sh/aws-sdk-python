"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthenticationResultType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.integer_type
    import aws_sdk_cognito_identity_provider.types.new_device_metadata_type
    import aws_sdk_cognito_identity_provider.types.string_type
    import aws_sdk_cognito_identity_provider.types.token_model_type


class AuthenticationResultType(TypedDict):
    access_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>Your user's access token.</p>"""
    expires_in: "aws_sdk_cognito_identity_provider.types.integer_type.IntegerType"
    """<p>The expiration period of the authentication result in seconds.</p>"""
    token_type: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The intended use of the token, for example <code>Bearer</code>.</p>"""
    refresh_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>Your user's refresh token.</p>"""
    id_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>Your user's ID token.</p>"""
    new_device_metadata: NotRequired[
        "aws_sdk_cognito_identity_provider.types.new_device_metadata_type.NewDeviceMetadataType"
    ]
    """<p>The new device metadata from an authentication result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationResultType) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    out["ExpiresIn"] = value.get("expires_in", 0)
    if "token_type" in value:
        out["TokenType"] = value["token_type"]
    if "refresh_token" in value:
        out["RefreshToken"] = value["refresh_token"]
    if "id_token" in value:
        out["IdToken"] = value["id_token"]
    if "new_device_metadata" in value:
        import aws_sdk_cognito_identity_provider.types.new_device_metadata_type

        out["NewDeviceMetadata"] = (
            aws_sdk_cognito_identity_provider.types.new_device_metadata_type.serialize_aws_json_1_1(
                value["new_device_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationResultType:
    out: AuthenticationResultType = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    if "ExpiresIn" in data:
        out["expires_in"] = data["ExpiresIn"]
    else:
        out["expires_in"] = 0
    if "TokenType" in data:
        out["token_type"] = data["TokenType"]
    if "RefreshToken" in data:
        out["refresh_token"] = data["RefreshToken"]
    if "IdToken" in data:
        out["id_token"] = data["IdToken"]
    if "NewDeviceMetadata" in data:
        import aws_sdk_cognito_identity_provider.types.new_device_metadata_type

        out["new_device_metadata"] = (
            aws_sdk_cognito_identity_provider.types.new_device_metadata_type.deserialize_aws_json_1_1(
                data["NewDeviceMetadata"]
            )
        )
    return out
