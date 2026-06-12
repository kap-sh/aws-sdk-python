"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUICustomizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.css_type
    import aws_sdk_cognito_identity_provider.types.image_file_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class SetUICustomizationRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to apply branding to the classic hosted UI.</p>"""
    client_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client that you want to customize. To apply a default style to all app clients not configured with client-level branding, set this parameter value to <code>ALL</code>.</p>"""
    css: NotRequired["aws_sdk_cognito_identity_provider.types.css_type.CSSType"]
    """<p>A plaintext CSS file that contains the custom fields that you want to apply to your user pool or app client. To download a template, go to the Amazon Cognito console. Navigate to your user pool <i>App clients</i> tab, select <i>Login pages</i>, edit <i>Hosted UI (classic) style</i>, and select the link to <code>CSS template.css</code>.</p>"""
    image_file: NotRequired[
        "aws_sdk_cognito_identity_provider.types.image_file_type.ImageFileType"
    ]
    """<p>The image that you want to set as your login in the classic hosted UI, as a Base64-formatted binary object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUICustomizationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "css" in value:
        out["CSS"] = value["css"]
    if "image_file" in value:
        import aws_sdk_cognito_identity_provider.types.image_file_type

        out["ImageFile"] = (
            aws_sdk_cognito_identity_provider.types.image_file_type.serialize_aws_json_1_1(
                value["image_file"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUICustomizationRequest:
    out: SetUICustomizationRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("SetUICustomizationRequest.user_pool_id required")
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "CSS" in data:
        out["css"] = data["CSS"]
    if "ImageFile" in data:
        import aws_sdk_cognito_identity_provider.types.image_file_type

        out["image_file"] = (
            aws_sdk_cognito_identity_provider.types.image_file_type.deserialize_aws_json_1_1(
                data["ImageFile"]
            )
        )
    return out
