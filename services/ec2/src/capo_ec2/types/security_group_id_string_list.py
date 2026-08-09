"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_id

SecurityGroupIdStringList: TypeAlias = list[
    "capo_ec2.types.security_group_id.SecurityGroupId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupIdStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> SecurityGroupIdStringList:
    out: SecurityGroupIdStringList = []
    for child in el.findall("SecurityGroupId"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SecurityGroupIdStringList:
    out: SecurityGroupIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
