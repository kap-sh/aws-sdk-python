"""Generated from Smithy shape ``com.amazonaws.rds#DBSecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.ec2_security_group_list
    import aws_sdk_rds.types.ip_range_list
    import aws_sdk_rds.types.string


class DBSecurityGroup(TypedDict):
    owner_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Provides the Amazon Web Services ID of the owner of a specific DB security group.</p>"""
    db_security_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Specifies the name of the DB security group.</p>"""
    db_security_group_description: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Provides the description of the DB security group.</p>"""
    vpc_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Provides the VpcId of the DB security group.</p>"""
    ec2_security_groups: NotRequired[
        "aws_sdk_rds.types.ec2_security_group_list.EC2SecurityGroupList"
    ]
    """<p>Contains a list of <code>EC2SecurityGroup</code> elements.</p>"""
    ip_ranges: NotRequired["aws_sdk_rds.types.ip_range_list.IPRangeList"]
    """<p>Contains a list of <code>IPRange</code> elements.</p>"""
    db_security_group_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "db_security_group_name" in value:
        pairs.append(
            (f"{prefix}.DBSecurityGroupName", str(value["db_security_group_name"]))
        )
    if "db_security_group_description" in value:
        pairs.append(
            (
                f"{prefix}.DBSecurityGroupDescription",
                str(value["db_security_group_description"]),
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "ec2_security_groups" in value:
        import aws_sdk_rds.types.ec2_security_group_list

        aws_sdk_rds.types.ec2_security_group_list.serialize_query(
            value["ec2_security_groups"], pairs, f"{prefix}.EC2SecurityGroups"
        )
    if "ip_ranges" in value:
        import aws_sdk_rds.types.ip_range_list

        aws_sdk_rds.types.ip_range_list.serialize_query(
            value["ip_ranges"], pairs, f"{prefix}.IPRanges"
        )
    if "db_security_group_arn" in value:
        pairs.append(
            (f"{prefix}.DBSecurityGroupArn", str(value["db_security_group_arn"]))
        )


def deserialize_query(el: Element) -> DBSecurityGroup:
    out: DBSecurityGroup = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_db_security_group_name = el.find("DBSecurityGroupName")
    if child_db_security_group_name is not None:
        out["db_security_group_name"] = str(child_db_security_group_name.text or "")
    child_db_security_group_description = el.find("DBSecurityGroupDescription")
    if child_db_security_group_description is not None:
        out["db_security_group_description"] = str(
            child_db_security_group_description.text or ""
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_ec2_security_groups = el.find("EC2SecurityGroups")
    if child_ec2_security_groups is not None:
        import aws_sdk_rds.types.ec2_security_group_list

        out["ec2_security_groups"] = (
            aws_sdk_rds.types.ec2_security_group_list.deserialize_query(
                child_ec2_security_groups
            )
        )
    child_ip_ranges = el.find("IPRanges")
    if child_ip_ranges is not None:
        import aws_sdk_rds.types.ip_range_list

        out["ip_ranges"] = aws_sdk_rds.types.ip_range_list.deserialize_query(
            child_ip_ranges
        )
    child_db_security_group_arn = el.find("DBSecurityGroupArn")
    if child_db_security_group_arn is not None:
        out["db_security_group_arn"] = str(child_db_security_group_arn.text or "")
    return out
