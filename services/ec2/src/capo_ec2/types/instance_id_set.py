"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_id

InstanceIdSet: TypeAlias = list["capo_ec2.types.instance_id.InstanceId"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIdSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> InstanceIdSet:
    out: InstanceIdSet = []
    for child in el.findall("item"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceIdSet:
    out: InstanceIdSet = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
