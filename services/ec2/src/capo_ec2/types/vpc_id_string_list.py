"""Generated from Smithy shape ``com.amazonaws.ec2#VpcIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_id

VpcIdStringList: TypeAlias = list["capo_ec2.types.vpc_id.VpcId"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcIdStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> VpcIdStringList:
    out: VpcIdStringList = []
    for child in el.findall("VpcId"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VpcIdStringList:
    out: VpcIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
