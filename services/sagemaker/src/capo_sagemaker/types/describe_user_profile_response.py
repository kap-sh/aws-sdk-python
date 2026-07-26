"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeUserProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.efs_uid
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.single_sign_on_user_identifier
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.user_profile_arn
    import capo_sagemaker.types.user_profile_name
    import capo_sagemaker.types.user_profile_status
    import capo_sagemaker.types.user_settings


class DescribeUserProfileResponse(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the domain that contains the profile.</p>"""
    user_profile_arn: NotRequired[
        "capo_sagemaker.types.user_profile_arn.UserProfileArn"
    ]
    """<p>The user profile Amazon Resource Name (ARN).</p>"""
    user_profile_name: NotRequired[
        "capo_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name.</p>"""
    home_efs_file_system_uid: NotRequired["capo_sagemaker.types.efs_uid.EfsUid"]
    """<p>The ID of the user's profile in the Amazon Elastic File System volume.</p>"""
    status: NotRequired["capo_sagemaker.types.user_profile_status.UserProfileStatus"]
    """<p>The status.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last modified time.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason.</p>"""
    single_sign_on_user_identifier: NotRequired[
        "capo_sagemaker.types.single_sign_on_user_identifier.SingleSignOnUserIdentifier"
    ]
    """<p>The IAM Identity Center user identifier.</p>"""
    single_sign_on_user_value: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The IAM Identity Center user value.</p>"""
    user_settings: NotRequired["capo_sagemaker.types.user_settings.UserSettings"]
    """<p>A collection of settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserProfileResponse) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_arn" in value:
        out["UserProfileArn"] = value["user_profile_arn"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "home_efs_file_system_uid" in value:
        out["HomeEfsFileSystemUid"] = value["home_efs_file_system_uid"]
    if "status" in value:
        import capo_sagemaker.types.user_profile_status

        out["Status"] = capo_sagemaker.types.user_profile_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "single_sign_on_user_identifier" in value:
        out["SingleSignOnUserIdentifier"] = value["single_sign_on_user_identifier"]
    if "single_sign_on_user_value" in value:
        out["SingleSignOnUserValue"] = value["single_sign_on_user_value"]
    if "user_settings" in value:
        import capo_sagemaker.types.user_settings

        out["UserSettings"] = capo_sagemaker.types.user_settings.serialize_aws_json_1_1(
            value["user_settings"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserProfileResponse:
    out: DescribeUserProfileResponse = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileArn" in data:
        out["user_profile_arn"] = data["UserProfileArn"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "HomeEfsFileSystemUid" in data:
        out["home_efs_file_system_uid"] = data["HomeEfsFileSystemUid"]
    if "Status" in data:
        import capo_sagemaker.types.user_profile_status

        out["status"] = (
            capo_sagemaker.types.user_profile_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "SingleSignOnUserIdentifier" in data:
        out["single_sign_on_user_identifier"] = data["SingleSignOnUserIdentifier"]
    if "SingleSignOnUserValue" in data:
        out["single_sign_on_user_value"] = data["SingleSignOnUserValue"]
    if "UserSettings" in data:
        import capo_sagemaker.types.user_settings

        out["user_settings"] = (
            capo_sagemaker.types.user_settings.deserialize_aws_json_1_1(
                data["UserSettings"]
            )
        )
    return out
