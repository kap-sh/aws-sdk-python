"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeSpaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.efs_uid
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.non_empty_string64
    import capo_sagemaker.types.ownership_settings
    import capo_sagemaker.types.space_arn
    import capo_sagemaker.types.space_name
    import capo_sagemaker.types.space_settings
    import capo_sagemaker.types.space_sharing_settings
    import capo_sagemaker.types.space_status
    import capo_sagemaker.types.string1024


class DescribeSpaceResponse(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the associated domain.</p>"""
    space_arn: NotRequired["capo_sagemaker.types.space_arn.SpaceArn"]
    """<p>The space's Amazon Resource Name (ARN).</p>"""
    space_name: NotRequired["capo_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    home_efs_file_system_uid: NotRequired["capo_sagemaker.types.efs_uid.EfsUid"]
    """<p>The ID of the space's profile in the Amazon EFS volume.</p>"""
    status: NotRequired["capo_sagemaker.types.space_status.SpaceStatus"]
    """<p>The status.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last modified time.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason.</p>"""
    space_settings: NotRequired["capo_sagemaker.types.space_settings.SpaceSettings"]
    """<p>A collection of space settings.</p>"""
    ownership_settings: NotRequired[
        "capo_sagemaker.types.ownership_settings.OwnershipSettings"
    ]
    """<p>The collection of ownership settings for a space.</p>"""
    space_sharing_settings: NotRequired[
        "capo_sagemaker.types.space_sharing_settings.SpaceSharingSettings"
    ]
    """<p>The collection of space sharing settings for a space.</p>"""
    space_display_name: NotRequired[
        "capo_sagemaker.types.non_empty_string64.NonEmptyString64"
    ]
    """<p>The name of the space that appears in the Amazon SageMaker Studio UI.</p>"""
    url: NotRequired["capo_sagemaker.types.string1024.String1024"]
    """<p>Returns the URL of the space. If the space is created with Amazon Web Services IAM Identity Center (Successor to Amazon Web Services Single Sign-On) authentication, users can navigate to the URL after appending the respective redirect parameter for the application type to be federated through Amazon Web Services IAM Identity Center.</p> <p>The following application types are supported:</p> <ul> <li> <p>Studio Classic: <code>&amp;redirect=JupyterServer</code> </p> </li> <li> <p>JupyterLab: <code>&amp;redirect=JupyterLab</code> </p> </li> <li> <p>Code Editor, based on Code-OSS, Visual Studio Code - Open Source: <code>&amp;redirect=CodeEditor</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSpaceResponse) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "space_arn" in value:
        out["SpaceArn"] = value["space_arn"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "home_efs_file_system_uid" in value:
        out["HomeEfsFileSystemUid"] = value["home_efs_file_system_uid"]
    if "status" in value:
        import capo_sagemaker.types.space_status

        out["Status"] = capo_sagemaker.types.space_status.serialize_aws_json_1_1(
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
    if "space_settings" in value:
        import capo_sagemaker.types.space_settings

        out["SpaceSettings"] = (
            capo_sagemaker.types.space_settings.serialize_aws_json_1_1(
                value["space_settings"]
            )
        )
    if "ownership_settings" in value:
        import capo_sagemaker.types.ownership_settings

        out["OwnershipSettings"] = (
            capo_sagemaker.types.ownership_settings.serialize_aws_json_1_1(
                value["ownership_settings"]
            )
        )
    if "space_sharing_settings" in value:
        import capo_sagemaker.types.space_sharing_settings

        out["SpaceSharingSettings"] = (
            capo_sagemaker.types.space_sharing_settings.serialize_aws_json_1_1(
                value["space_sharing_settings"]
            )
        )
    if "space_display_name" in value:
        out["SpaceDisplayName"] = value["space_display_name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSpaceResponse:
    out: DescribeSpaceResponse = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "SpaceArn" in data:
        out["space_arn"] = data["SpaceArn"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "HomeEfsFileSystemUid" in data:
        out["home_efs_file_system_uid"] = data["HomeEfsFileSystemUid"]
    if "Status" in data:
        import capo_sagemaker.types.space_status

        out["status"] = capo_sagemaker.types.space_status.deserialize_aws_json_1_1(
            data["Status"]
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
    if "SpaceSettings" in data:
        import capo_sagemaker.types.space_settings

        out["space_settings"] = (
            capo_sagemaker.types.space_settings.deserialize_aws_json_1_1(
                data["SpaceSettings"]
            )
        )
    if "OwnershipSettings" in data:
        import capo_sagemaker.types.ownership_settings

        out["ownership_settings"] = (
            capo_sagemaker.types.ownership_settings.deserialize_aws_json_1_1(
                data["OwnershipSettings"]
            )
        )
    if "SpaceSharingSettings" in data:
        import capo_sagemaker.types.space_sharing_settings

        out["space_sharing_settings"] = (
            capo_sagemaker.types.space_sharing_settings.deserialize_aws_json_1_1(
                data["SpaceSharingSettings"]
            )
        )
    if "SpaceDisplayName" in data:
        out["space_display_name"] = data["SpaceDisplayName"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
