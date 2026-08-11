"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_secondary_interface

InstanceSecondaryInterfaceList: TypeAlias = list[
    "capo_ec2.types.instance_secondary_interface.InstanceSecondaryInterface"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSecondaryInterfaceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_secondary_interface

        capo_ec2.types.instance_secondary_interface.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceSecondaryInterfaceList:
    import capo_ec2.types.instance_secondary_interface

    out: InstanceSecondaryInterfaceList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.instance_secondary_interface.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> InstanceSecondaryInterfaceList:
    import capo_ec2.types.instance_secondary_interface

    out: InstanceSecondaryInterfaceList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.instance_secondary_interface.deserialize_ec2_query(child)
        )
    return out
