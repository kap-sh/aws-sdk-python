"""Generated from Smithy shape ``com.amazonaws.rds#EC2SecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.ec2_security_group

EC2SecurityGroupList: TypeAlias = list[
    "capo_rds.types.ec2_security_group.EC2SecurityGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EC2SecurityGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.ec2_security_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.ec2_security_group.serialize_query(
            item, pairs, f"{prefix}.EC2SecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> EC2SecurityGroupList:
    import capo_rds.types.ec2_security_group

    out: EC2SecurityGroupList = []
    for child in el.findall("EC2SecurityGroup"):
        out.append(capo_rds.types.ec2_security_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EC2SecurityGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.ec2_security_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.ec2_security_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EC2SecurityGroupList:
    import capo_rds.types.ec2_security_group

    out: EC2SecurityGroupList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.ec2_security_group.deserialize_query(child))
    return out
