"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_name_list_type
    import aws_sdk_cognito_identity_provider.types.token_model_type


class DeleteUserAttributesRequest(TypedDict, closed=True):
    user_attribute_names: "aws_sdk_cognito_identity_provider.types.attribute_name_list_type.AttributeNameListType"
    """<p>An array of strings representing the user attribute names you want to delete.</p> <p>For custom attributes, you must prepend the <code>custom:</code> prefix to the attribute name, for example <code>custom:department</code>.</p>"""
    access_token: (
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    )
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserAttributesRequest) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.attribute_name_list_type

    out["UserAttributeNames"] = (
        aws_sdk_cognito_identity_provider.types.attribute_name_list_type.serialize_aws_json_1_1(
            value["user_attribute_names"]
        )
    )
    out["AccessToken"] = value["access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserAttributesRequest:
    out: DeleteUserAttributesRequest = {}  # type: ignore[typeddict-item]
    if "UserAttributeNames" in data:
        import aws_sdk_cognito_identity_provider.types.attribute_name_list_type

        out["user_attribute_names"] = (
            aws_sdk_cognito_identity_provider.types.attribute_name_list_type.deserialize_aws_json_1_1(
                data["UserAttributeNames"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteUserAttributesRequest.user_attribute_names required"
        )
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("DeleteUserAttributesRequest.access_token required")
    return out
