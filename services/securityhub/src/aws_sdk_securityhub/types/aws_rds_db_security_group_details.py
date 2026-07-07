"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSecurityGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_security_group_ec2_security_groups
    import aws_sdk_securityhub.types.aws_rds_db_security_group_ip_ranges
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbSecurityGroupDetails(TypedDict, closed=True):
    db_security_group_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN for the DB security group.</p>"""
    db_security_group_description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Provides the description of the DB security group.</p>"""
    db_security_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the name of the DB security group.</p>"""
    ec2_security_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_security_group_ec2_security_groups.AwsRdsDbSecurityGroupEc2SecurityGroups"
    ]
    """<p>Contains a list of EC2 security groups.</p>"""
    ip_ranges: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_security_group_ip_ranges.AwsRdsDbSecurityGroupIpRanges"
    ]
    """<p>Contains a list of IP ranges.</p>"""
    owner_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Provides the Amazon Web Services ID of the owner of a specific DB security group.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Provides VPC ID associated with the DB security group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSecurityGroupDetails) -> dict:
    out: dict = {}
    if "db_security_group_arn" in value:
        out["DbSecurityGroupArn"] = value["db_security_group_arn"]
    if "db_security_group_description" in value:
        out["DbSecurityGroupDescription"] = value["db_security_group_description"]
    if "db_security_group_name" in value:
        out["DbSecurityGroupName"] = value["db_security_group_name"]
    if "ec2_security_groups" in value:
        import aws_sdk_securityhub.types.aws_rds_db_security_group_ec2_security_groups

        out["Ec2SecurityGroups"] = (
            aws_sdk_securityhub.types.aws_rds_db_security_group_ec2_security_groups.serialize_json(
                value["ec2_security_groups"]
            )
        )
    if "ip_ranges" in value:
        import aws_sdk_securityhub.types.aws_rds_db_security_group_ip_ranges

        out["IpRanges"] = (
            aws_sdk_securityhub.types.aws_rds_db_security_group_ip_ranges.serialize_json(
                value["ip_ranges"]
            )
        )
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbSecurityGroupDetails:
    out: AwsRdsDbSecurityGroupDetails = {}  # type: ignore[typeddict-item]
    if "DbSecurityGroupArn" in data:
        out["db_security_group_arn"] = data["DbSecurityGroupArn"]
    if "DbSecurityGroupDescription" in data:
        out["db_security_group_description"] = data["DbSecurityGroupDescription"]
    if "DbSecurityGroupName" in data:
        out["db_security_group_name"] = data["DbSecurityGroupName"]
    if "Ec2SecurityGroups" in data:
        import aws_sdk_securityhub.types.aws_rds_db_security_group_ec2_security_groups

        out["ec2_security_groups"] = (
            aws_sdk_securityhub.types.aws_rds_db_security_group_ec2_security_groups.deserialize_json(
                data["Ec2SecurityGroups"]
            )
        )
    if "IpRanges" in data:
        import aws_sdk_securityhub.types.aws_rds_db_security_group_ip_ranges

        out["ip_ranges"] = (
            aws_sdk_securityhub.types.aws_rds_db_security_group_ip_ranges.deserialize_json(
                data["IpRanges"]
            )
        )
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
