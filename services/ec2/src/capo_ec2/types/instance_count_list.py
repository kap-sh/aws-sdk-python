"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCountList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_count

InstanceCountList: TypeAlias = list["capo_ec2.types.instance_count.InstanceCount"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceCountList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_count

        capo_ec2.types.instance_count.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceCountList:
    import capo_ec2.types.instance_count

    out: InstanceCountList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_count.deserialize_ec2_query(child))
    return out
