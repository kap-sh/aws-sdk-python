"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationFsxLustreRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.ec2_security_group_arn_list
    import aws_sdk_datasync.types.fsx_filesystem_arn
    import aws_sdk_datasync.types.fsx_lustre_subdirectory
    import aws_sdk_datasync.types.input_tag_list


class CreateLocationFsxLustreRequest(TypedDict):
    fsx_filesystem_arn: "aws_sdk_datasync.types.fsx_filesystem_arn.FsxFilesystemArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the FSx for Lustre file system.</p>"""
    security_group_arns: (
        "aws_sdk_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    )
    """<p>Specifies the Amazon Resource Names (ARNs) of up to five security groups that provide access to your FSx for Lustre file system.</p> <p>The security groups must be able to access the file system's ports. The file system must also allow access from the security groups. For information about file system access, see the <a href=\"https://docs.aws.amazon.com/fsx/latest/LustreGuide/limit-access-security-groups.html\"> <i>Amazon FSx for Lustre User Guide</i> </a>.</p>"""
    subdirectory: NotRequired[
        "aws_sdk_datasync.types.fsx_lustre_subdirectory.FsxLustreSubdirectory"
    ]
    """<p>Specifies a mount path for your FSx for Lustre file system. The path can include subdirectories.</p> <p>When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes data to the mount path. If you don't include this parameter, DataSync uses the file system's root directory (<code>/</code>).</p>"""
    tags: NotRequired["aws_sdk_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationFsxLustreRequest) -> dict:
    out: dict = {}
    out["FsxFilesystemArn"] = value["fsx_filesystem_arn"]
    import aws_sdk_datasync.types.ec2_security_group_arn_list

    out["SecurityGroupArns"] = (
        aws_sdk_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
            value["security_group_arns"]
        )
    )
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "tags" in value:
        import aws_sdk_datasync.types.input_tag_list

        out["Tags"] = aws_sdk_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationFsxLustreRequest:
    out: CreateLocationFsxLustreRequest = {}  # type: ignore[typeddict-item]
    if "FsxFilesystemArn" in data:
        out["fsx_filesystem_arn"] = data["FsxFilesystemArn"]
    else:
        raise DeserializationError(
            "CreateLocationFsxLustreRequest.fsx_filesystem_arn required"
        )
    if "SecurityGroupArns" in data:
        import aws_sdk_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            aws_sdk_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLocationFsxLustreRequest.security_group_arns required"
        )
    if "Subdirectory" in data:
        out["subdirectory"] = data["Subdirectory"]
    if "Tags" in data:
        import aws_sdk_datasync.types.input_tag_list

        out["tags"] = aws_sdk_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
