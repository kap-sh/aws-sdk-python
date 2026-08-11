"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBlockDeviceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_block_device_mapping

InstanceBlockDeviceMappingList: TypeAlias = list[
    "capo_ec2.types.instance_block_device_mapping.InstanceBlockDeviceMapping"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceBlockDeviceMappingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_block_device_mapping

        capo_ec2.types.instance_block_device_mapping.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceBlockDeviceMappingList:
    import capo_ec2.types.instance_block_device_mapping

    out: InstanceBlockDeviceMappingList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.instance_block_device_mapping.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> InstanceBlockDeviceMappingList:
    import capo_ec2.types.instance_block_device_mapping

    out: InstanceBlockDeviceMappingList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.instance_block_device_mapping.deserialize_ec2_query(child)
        )
    return out
