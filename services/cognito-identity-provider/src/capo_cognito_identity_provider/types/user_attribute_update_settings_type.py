"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserAttributeUpdateSettingsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attributes_require_verification_before_update_type


class UserAttributeUpdateSettingsType(TypedDict, closed=True):
    attributes_require_verification_before_update: NotRequired[
        "capo_cognito_identity_provider.types.attributes_require_verification_before_update_type.AttributesRequireVerificationBeforeUpdateType"
    ]
    """<p>Requires that your user verifies their email address, phone number, or both before Amazon Cognito updates the value of that attribute. When you update a user attribute that has this option activated, Amazon Cognito sends a verification message to the new phone number or email address. Amazon Cognito doesn’t change the value of the attribute until your user responds to the verification message and confirms the new value.</p> <p>When <code>AttributesRequireVerificationBeforeUpdate</code> is false, your user pool doesn't require that your users verify attribute changes before Amazon Cognito updates them. In a user pool where <code>AttributesRequireVerificationBeforeUpdate</code> is false, API operations that change attribute values can immediately update a user’s <code>email</code> or <code>phone_number</code> attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserAttributeUpdateSettingsType) -> dict:
    out: dict = {}
    if "attributes_require_verification_before_update" in value:
        import capo_cognito_identity_provider.types.attributes_require_verification_before_update_type

        out["AttributesRequireVerificationBeforeUpdate"] = (
            capo_cognito_identity_provider.types.attributes_require_verification_before_update_type.serialize_aws_json_1_1(
                value["attributes_require_verification_before_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserAttributeUpdateSettingsType:
    out: UserAttributeUpdateSettingsType = {}  # type: ignore[typeddict-item]
    if "AttributesRequireVerificationBeforeUpdate" in data:
        import capo_cognito_identity_provider.types.attributes_require_verification_before_update_type

        out["attributes_require_verification_before_update"] = (
            capo_cognito_identity_provider.types.attributes_require_verification_before_update_type.deserialize_aws_json_1_1(
                data["AttributesRequireVerificationBeforeUpdate"]
            )
        )
    return out
