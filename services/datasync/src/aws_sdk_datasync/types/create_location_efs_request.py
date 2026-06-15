"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationEfsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.ec2_config
    import aws_sdk_datasync.types.efs_access_point_arn
    import aws_sdk_datasync.types.efs_filesystem_arn
    import aws_sdk_datasync.types.efs_in_transit_encryption
    import aws_sdk_datasync.types.efs_subdirectory
    import aws_sdk_datasync.types.iam_role_arn
    import aws_sdk_datasync.types.input_tag_list


class CreateLocationEfsRequest(TypedDict):
    subdirectory: NotRequired["aws_sdk_datasync.types.efs_subdirectory.EfsSubdirectory"]
    r"""<p>Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or destination location).</p> <p>By default, DataSync uses the root directory (or <a href=\"https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html\">access point</a> if you provide one by using <code>AccessPointArn</code>). You can also include subdirectories using forward slashes (for example, <code>/path/to/folder</code>).</p>"""
    efs_filesystem_arn: "aws_sdk_datasync.types.efs_filesystem_arn.EfsFilesystemArn"
    """<p>Specifies the ARN for your Amazon EFS file system.</p>"""
    ec2_config: "aws_sdk_datasync.types.ec2_config.Ec2Config"
    r"""<p>Specifies the subnet and security groups DataSync uses to connect to one of your Amazon EFS file system's <a href=\"https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html\">mount targets</a>.</p>"""
    tags: NotRequired["aws_sdk_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies the key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.</p>"""
    access_point_arn: NotRequired[
        "aws_sdk_datasync.types.efs_access_point_arn.EfsAccessPointArn"
    ]
    r"""<p>Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to mount your Amazon EFS file system.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam\">Accessing restricted file systems</a>.</p>"""
    file_system_access_role_arn: NotRequired[
        "aws_sdk_datasync.types.iam_role_arn.IamRoleArn"
    ]
    r"""<p>Specifies an Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.</p> <p>For information on creating this role, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role\">Creating a DataSync IAM role for file system access</a>.</p>"""
    in_transit_encryption: NotRequired[
        "aws_sdk_datasync.types.efs_in_transit_encryption.EfsInTransitEncryption"
    ]
    """<p>Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it transfers data to or from your Amazon EFS file system.</p> <p>If you specify an access point using <code>AccessPointArn</code> or an IAM role using <code>FileSystemAccessRoleArn</code>, you must set this parameter to <code>TLS1_2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationEfsRequest) -> dict:
    out: dict = {}
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    out["EfsFilesystemArn"] = value["efs_filesystem_arn"]
    import aws_sdk_datasync.types.ec2_config

    out["Ec2Config"] = aws_sdk_datasync.types.ec2_config.serialize_aws_json_1_1(
        value["ec2_config"]
    )
    if "tags" in value:
        import aws_sdk_datasync.types.input_tag_list

        out["Tags"] = aws_sdk_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "access_point_arn" in value:
        out["AccessPointArn"] = value["access_point_arn"]
    if "file_system_access_role_arn" in value:
        out["FileSystemAccessRoleArn"] = value["file_system_access_role_arn"]
    if "in_transit_encryption" in value:
        import aws_sdk_datasync.types.efs_in_transit_encryption

        out["InTransitEncryption"] = (
            aws_sdk_datasync.types.efs_in_transit_encryption.serialize_aws_json_1_1(
                value["in_transit_encryption"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationEfsRequest:
    out: CreateLocationEfsRequest = {}  # type: ignore[typeddict-item]
    if "Subdirectory" in data:
        out["subdirectory"] = data["Subdirectory"]
    if "EfsFilesystemArn" in data:
        out["efs_filesystem_arn"] = data["EfsFilesystemArn"]
    else:
        raise DeserializationError(
            "CreateLocationEfsRequest.efs_filesystem_arn required"
        )
    if "Ec2Config" in data:
        import aws_sdk_datasync.types.ec2_config

        out["ec2_config"] = aws_sdk_datasync.types.ec2_config.deserialize_aws_json_1_1(
            data["Ec2Config"]
        )
    else:
        raise DeserializationError("CreateLocationEfsRequest.ec2_config required")
    if "Tags" in data:
        import aws_sdk_datasync.types.input_tag_list

        out["tags"] = aws_sdk_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "AccessPointArn" in data:
        out["access_point_arn"] = data["AccessPointArn"]
    if "FileSystemAccessRoleArn" in data:
        out["file_system_access_role_arn"] = data["FileSystemAccessRoleArn"]
    if "InTransitEncryption" in data:
        import aws_sdk_datasync.types.efs_in_transit_encryption

        out["in_transit_encryption"] = (
            aws_sdk_datasync.types.efs_in_transit_encryption.deserialize_aws_json_1_1(
                data["InTransitEncryption"]
            )
        )
    return out
