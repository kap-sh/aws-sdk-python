"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminDeleteUserAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_name_list_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type
    import aws_sdk_cognito_identity_provider.types.username_type


class AdminDeleteUserAttributesRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to delete user attributes.</p>"""
    username: "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    user_attribute_names: "aws_sdk_cognito_identity_provider.types.attribute_name_list_type.AttributeNameListType"
    """<p>An array of strings representing the user attribute names you want to delete.</p> <p>For custom attributes, you must prepend the <code>custom:</code> prefix to the attribute name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminDeleteUserAttributesRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    import aws_sdk_cognito_identity_provider.types.attribute_name_list_type

    out["UserAttributeNames"] = (
        aws_sdk_cognito_identity_provider.types.attribute_name_list_type.serialize_aws_json_1_1(
            value["user_attribute_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminDeleteUserAttributesRequest:
    out: AdminDeleteUserAttributesRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "AdminDeleteUserAttributesRequest.user_pool_id required"
        )
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminDeleteUserAttributesRequest.username required")
    if "UserAttributeNames" in data:
        import aws_sdk_cognito_identity_provider.types.attribute_name_list_type

        out["user_attribute_names"] = (
            aws_sdk_cognito_identity_provider.types.attribute_name_list_type.deserialize_aws_json_1_1(
                data["UserAttributeNames"]
            )
        )
    else:
        raise DeserializationError(
            "AdminDeleteUserAttributesRequest.user_attribute_names required"
        )
    return out
