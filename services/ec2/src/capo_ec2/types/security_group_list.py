"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group

SecurityGroupList: TypeAlias = list["capo_ec2.types.security_group.SecurityGroup"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.security_group

        capo_ec2.types.security_group.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> SecurityGroupList:
    import capo_ec2.types.security_group

    out: SecurityGroupList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.security_group.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SecurityGroupList:
    import capo_ec2.types.security_group

    out: SecurityGroupList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.security_group.deserialize_ec2_query(child))
    return out
