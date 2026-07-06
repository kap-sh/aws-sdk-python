"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeUserProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.efs_uid
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.single_sign_on_user_identifier
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.user_profile_arn
    import aws_sdk_sagemaker.types.user_profile_name
    import aws_sdk_sagemaker.types.user_profile_status
    import aws_sdk_sagemaker.types.user_settings


class DescribeUserProfileResponse(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the domain that contains the profile.</p>"""
    user_profile_arn: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_arn.UserProfileArn"
    ]
    """<p>The user profile Amazon Resource Name (ARN).</p>"""
    user_profile_name: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name.</p>"""
    home_efs_file_system_uid: NotRequired["aws_sdk_sagemaker.types.efs_uid.EfsUid"]
    """<p>The ID of the user's profile in the Amazon Elastic File System volume.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.user_profile_status.UserProfileStatus"]
    """<p>The status.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last modified time.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason.</p>"""
    single_sign_on_user_identifier: NotRequired[
        "aws_sdk_sagemaker.types.single_sign_on_user_identifier.SingleSignOnUserIdentifier"
    ]
    """<p>The IAM Identity Center user identifier.</p>"""
    single_sign_on_user_value: NotRequired[
        "aws_sdk_sagemaker.types.string256.String256"
    ]
    """<p>The IAM Identity Center user value.</p>"""
    user_settings: NotRequired["aws_sdk_sagemaker.types.user_settings.UserSettings"]
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
        import aws_sdk_sagemaker.types.user_profile_status

        out["Status"] = (
            aws_sdk_sagemaker.types.user_profile_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "single_sign_on_user_identifier" in value:
        out["SingleSignOnUserIdentifier"] = value["single_sign_on_user_identifier"]
    if "single_sign_on_user_value" in value:
        out["SingleSignOnUserValue"] = value["single_sign_on_user_value"]
    if "user_settings" in value:
        import aws_sdk_sagemaker.types.user_settings

        out["UserSettings"] = (
            aws_sdk_sagemaker.types.user_settings.serialize_aws_json_1_1(
                value["user_settings"]
            )
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
        import aws_sdk_sagemaker.types.user_profile_status

        out["status"] = (
            aws_sdk_sagemaker.types.user_profile_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
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
        import aws_sdk_sagemaker.types.user_settings

        out["user_settings"] = (
            aws_sdk_sagemaker.types.user_settings.deserialize_aws_json_1_1(
                data["UserSettings"]
            )
        )
    return out
