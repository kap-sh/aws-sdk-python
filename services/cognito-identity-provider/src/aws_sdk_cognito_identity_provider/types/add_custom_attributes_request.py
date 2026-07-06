"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AddCustomAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.custom_attributes_list_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class AddCustomAttributesRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to add custom attributes.</p>"""
    custom_attributes: "aws_sdk_cognito_identity_provider.types.custom_attributes_list_type.CustomAttributesListType"
    """<p>An array of custom attribute names and other properties. Sets the following characteristics:</p> <dl> <dt>AttributeDataType</dt> <dd> <p>The expected data type. Can be a string, a number, a date and time, or a boolean.</p> </dd> <dt>Mutable</dt> <dd> <p>If true, you can grant app clients write access to the attribute value. If false, the attribute value can only be set up on sign-up or administrator creation of users.</p> </dd> <dt>Name</dt> <dd> <p>The attribute name. For an attribute like <code>custom:myAttribute</code>, enter <code>myAttribute</code> for this field.</p> </dd> <dt>Required</dt> <dd> <p>When true, users who sign up or are created must set a value for the attribute.</p> </dd> <dt>NumberAttributeConstraints</dt> <dd> <p>The minimum and maximum length of accepted values for a <code>Number</code>-type attribute.</p> </dd> <dt>StringAttributeConstraints</dt> <dd> <p>The minimum and maximum length of accepted values for a <code>String</code>-type attribute.</p> </dd> <dt>DeveloperOnlyAttribute</dt> <dd> <p>This legacy option creates an attribute with a <code>dev:</code> prefix. You can only set the value of a developer-only attribute with administrative IAM credentials.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddCustomAttributesRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import aws_sdk_cognito_identity_provider.types.custom_attributes_list_type

    out["CustomAttributes"] = (
        aws_sdk_cognito_identity_provider.types.custom_attributes_list_type.serialize_aws_json_1_1(
            value["custom_attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddCustomAttributesRequest:
    out: AddCustomAttributesRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("AddCustomAttributesRequest.user_pool_id required")
    if "CustomAttributes" in data:
        import aws_sdk_cognito_identity_provider.types.custom_attributes_list_type

        out["custom_attributes"] = (
            aws_sdk_cognito_identity_provider.types.custom_attributes_list_type.deserialize_aws_json_1_1(
                data["CustomAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "AddCustomAttributesRequest.custom_attributes required"
        )
    return out
