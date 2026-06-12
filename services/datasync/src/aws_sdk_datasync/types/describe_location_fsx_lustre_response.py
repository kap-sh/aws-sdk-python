"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationFsxLustreResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.ec2_security_group_arn_list
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.location_uri
    import aws_sdk_datasync.types.time


class DescribeLocationFsxLustreResponse(TypedDict):
    location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The Amazon Resource Name (ARN) of the FSx for Lustre location that was described.</p>"""
    location_uri: NotRequired["aws_sdk_datasync.types.location_uri.LocationUri"]
    """<p>The URI of the FSx for Lustre location that was described.</p>"""
    security_group_arns: NotRequired[
        "aws_sdk_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the security groups that are configured for the FSx for Lustre file system.</p>"""
    creation_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the FSx for Lustre location was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationFsxLustreResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "security_group_arns" in value:
        import aws_sdk_datasync.types.ec2_security_group_arn_list

        out["SecurityGroupArns"] = (
            aws_sdk_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
                value["security_group_arns"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_datasync.types.time

        out["CreationTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationFsxLustreResponse:
    out: DescribeLocationFsxLustreResponse = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "SecurityGroupArns" in data:
        import aws_sdk_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            aws_sdk_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_datasync.types.time

        out["creation_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
