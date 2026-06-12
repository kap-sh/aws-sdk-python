"""Generated from Smithy shape ``com.amazonaws.elasticache#EC2SecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class EC2SecurityGroup(TypedDict):
    status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The status of the Amazon EC2 security group.</p>"""
    ec2_security_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Amazon EC2 security group.</p>"""
    ec2_security_group_owner_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon account ID of the Amazon EC2 security group owner.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EC2SecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "ec2_security_group_name" in value:
        pairs.append(
            (f"{prefix}.EC2SecurityGroupName", str(value["ec2_security_group_name"]))
        )
    if "ec2_security_group_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.EC2SecurityGroupOwnerId",
                str(value["ec2_security_group_owner_id"]),
            )
        )


def deserialize_query(el: Element) -> EC2SecurityGroup:
    out: EC2SecurityGroup = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_ec2_security_group_name = el.find("EC2SecurityGroupName")
    if child_ec2_security_group_name is not None:
        out["ec2_security_group_name"] = str(child_ec2_security_group_name.text or "")
    child_ec2_security_group_owner_id = el.find("EC2SecurityGroupOwnerId")
    if child_ec2_security_group_owner_id is not None:
        out["ec2_security_group_owner_id"] = str(
            child_ec2_security_group_owner_id.text or ""
        )
    return out
