"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_acl_id

NetworkAclIdStringList: TypeAlias = list["capo_ec2.types.network_acl_id.NetworkAclId"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkAclIdStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> NetworkAclIdStringList:
    out: NetworkAclIdStringList = []
    for child in el.findall("item"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> NetworkAclIdStringList:
    out: NetworkAclIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
