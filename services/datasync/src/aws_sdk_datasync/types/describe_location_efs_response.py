"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationEfsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.ec2_config
    import aws_sdk_datasync.types.efs_access_point_arn
    import aws_sdk_datasync.types.efs_in_transit_encryption
    import aws_sdk_datasync.types.iam_role_arn
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.location_uri
    import aws_sdk_datasync.types.time


class DescribeLocationEfsResponse(TypedDict):
    location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the Amazon EFS file system location.</p>"""
    location_uri: NotRequired["aws_sdk_datasync.types.location_uri.LocationUri"]
    """<p>The URL of the Amazon EFS file system location.</p>"""
    ec2_config: NotRequired["aws_sdk_datasync.types.ec2_config.Ec2Config"]
    creation_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the location was created.</p>"""
    access_point_arn: NotRequired[
        "aws_sdk_datasync.types.efs_access_point_arn.EfsAccessPointArn"
    ]
    """<p>The ARN of the access point that DataSync uses to access the Amazon EFS file system.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam\">Accessing restricted file systems</a>.</p>"""
    file_system_access_role_arn: NotRequired[
        "aws_sdk_datasync.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role\">Creating a DataSync IAM role for file system access</a>.</p>"""
    in_transit_encryption: NotRequired[
        "aws_sdk_datasync.types.efs_in_transit_encryption.EfsInTransitEncryption"
    ]
    """<p>Indicates whether DataSync uses Transport Layer Security (TLS) encryption when transferring data to or from the Amazon EFS file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationEfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "ec2_config" in value:
        import aws_sdk_datasync.types.ec2_config

        out["Ec2Config"] = aws_sdk_datasync.types.ec2_config.serialize_aws_json_1_1(
            value["ec2_config"]
        )
    if "creation_time" in value:
        import aws_sdk_datasync.types.time

        out["CreationTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationEfsResponse:
    out: DescribeLocationEfsResponse = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "Ec2Config" in data:
        import aws_sdk_datasync.types.ec2_config

        out["ec2_config"] = aws_sdk_datasync.types.ec2_config.deserialize_aws_json_1_1(
            data["Ec2Config"]
        )
    if "CreationTime" in data:
        import aws_sdk_datasync.types.time

        out["creation_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
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
