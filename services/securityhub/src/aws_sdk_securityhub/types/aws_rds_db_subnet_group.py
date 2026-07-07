"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnets
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbSubnetGroup(TypedDict, closed=True):
    db_subnet_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the subnet group.</p>"""
    db_subnet_group_description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the subnet group.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The VPC ID of the subnet group.</p>"""
    subnet_group_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the subnet group.</p>"""
    subnets: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnets.AwsRdsDbSubnetGroupSubnets"
    ]
    """<p>A list of subnets in the subnet group.</p>"""
    db_subnet_group_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the subnet group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSubnetGroup) -> dict:
    out: dict = {}
    if "db_subnet_group_name" in value:
        out["DbSubnetGroupName"] = value["db_subnet_group_name"]
    if "db_subnet_group_description" in value:
        out["DbSubnetGroupDescription"] = value["db_subnet_group_description"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_group_status" in value:
        out["SubnetGroupStatus"] = value["subnet_group_status"]
    if "subnets" in value:
        import aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnets

        out["Subnets"] = (
            aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnets.serialize_json(
                value["subnets"]
            )
        )
    if "db_subnet_group_arn" in value:
        out["DbSubnetGroupArn"] = value["db_subnet_group_arn"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbSubnetGroup:
    out: AwsRdsDbSubnetGroup = {}  # type: ignore[typeddict-item]
    if "DbSubnetGroupName" in data:
        out["db_subnet_group_name"] = data["DbSubnetGroupName"]
    if "DbSubnetGroupDescription" in data:
        out["db_subnet_group_description"] = data["DbSubnetGroupDescription"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetGroupStatus" in data:
        out["subnet_group_status"] = data["SubnetGroupStatus"]
    if "Subnets" in data:
        import aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnets

        out["subnets"] = (
            aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnets.deserialize_json(
                data["Subnets"]
            )
        )
    if "DbSubnetGroupArn" in data:
        out["db_subnet_group_arn"] = data["DbSubnetGroupArn"]
    return out
