"""Generated from Smithy shape ``com.amazonaws.redshift#EC2SecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.ec2_security_group

EC2SecurityGroupList: TypeAlias = list[
    "capo_redshift.types.ec2_security_group.EC2SecurityGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EC2SecurityGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.ec2_security_group

    for n, item in enumerate(value, 1):
        capo_redshift.types.ec2_security_group.serialize_query(
            item, pairs, f"{prefix}.EC2SecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> EC2SecurityGroupList:
    import capo_redshift.types.ec2_security_group

    out: EC2SecurityGroupList = []
    for child in el.findall("EC2SecurityGroup"):
        out.append(capo_redshift.types.ec2_security_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EC2SecurityGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.ec2_security_group

    for n, item in enumerate(value, 1):
        capo_redshift.types.ec2_security_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EC2SecurityGroupList:
    import capo_redshift.types.ec2_security_group

    out: EC2SecurityGroupList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.ec2_security_group.deserialize_query(child))
    return out
