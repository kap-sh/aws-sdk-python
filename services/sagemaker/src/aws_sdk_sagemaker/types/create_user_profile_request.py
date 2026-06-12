"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateUserProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.single_sign_on_user_identifier
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.user_profile_name
    import aws_sdk_sagemaker.types.user_settings


class CreateUserProfileRequest(TypedDict):
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the associated Domain.</p>"""
    user_profile_name: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>A name for the UserProfile. This value is not case sensitive.</p>"""
    single_sign_on_user_identifier: NotRequired[
        "aws_sdk_sagemaker.types.single_sign_on_user_identifier.SingleSignOnUserIdentifier"
    ]
    """<p>A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is \"UserName\". If the Domain's AuthMode is IAM Identity Center, this field is required. If the Domain's AuthMode is not IAM Identity Center, this field cannot be specified. </p>"""
    single_sign_on_user_value: NotRequired[
        "aws_sdk_sagemaker.types.string256.String256"
    ]
    """<p>The username of the associated Amazon Web Services Single Sign-On User for this UserProfile. If the Domain's AuthMode is IAM Identity Center, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not IAM Identity Center, this field cannot be specified. </p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Each tag consists of a key and an optional value. Tag keys must be unique per resource.</p> <p>Tags that you specify for the User Profile are also added to all Apps that the User Profile launches.</p>"""
    user_settings: NotRequired["aws_sdk_sagemaker.types.user_settings.UserSettings"]
    """<p>A collection of settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserProfileRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "single_sign_on_user_identifier" in value:
        out["SingleSignOnUserIdentifier"] = value["single_sign_on_user_identifier"]
    if "single_sign_on_user_value" in value:
        out["SingleSignOnUserValue"] = value["single_sign_on_user_value"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "user_settings" in value:
        import aws_sdk_sagemaker.types.user_settings

        out["UserSettings"] = (
            aws_sdk_sagemaker.types.user_settings.serialize_aws_json_1_1(
                value["user_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserProfileRequest:
    out: CreateUserProfileRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "SingleSignOnUserIdentifier" in data:
        out["single_sign_on_user_identifier"] = data["SingleSignOnUserIdentifier"]
    if "SingleSignOnUserValue" in data:
        out["single_sign_on_user_value"] = data["SingleSignOnUserValue"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "UserSettings" in data:
        import aws_sdk_sagemaker.types.user_settings

        out["user_settings"] = (
            aws_sdk_sagemaker.types.user_settings.deserialize_aws_json_1_1(
                data["UserSettings"]
            )
        )
    return out
