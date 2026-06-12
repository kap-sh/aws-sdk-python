"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifyUserAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_name_type
    import aws_sdk_cognito_identity_provider.types.confirmation_code_type
    import aws_sdk_cognito_identity_provider.types.token_model_type


class VerifyUserAttributeRequest(TypedDict):
    access_token: (
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    )
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    attribute_name: (
        "aws_sdk_cognito_identity_provider.types.attribute_name_type.AttributeNameType"
    )
    """<p>The name of the attribute that you want to verify.</p>"""
    code: "aws_sdk_cognito_identity_provider.types.confirmation_code_type.ConfirmationCodeType"
    """<p>The verification code that your user pool sent to the added or changed attribute, for example the user's email address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyUserAttributeRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["AttributeName"] = value["attribute_name"]
    out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifyUserAttributeRequest:
    out: VerifyUserAttributeRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("VerifyUserAttributeRequest.access_token required")
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("VerifyUserAttributeRequest.attribute_name required")
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("VerifyUserAttributeRequest.code required")
    return out
