"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateBlockDeviceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_block_device_mapping

LaunchTemplateBlockDeviceMappingList: TypeAlias = list[
    "capo_ec2.types.launch_template_block_device_mapping.LaunchTemplateBlockDeviceMapping"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateBlockDeviceMappingList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_block_device_mapping

        capo_ec2.types.launch_template_block_device_mapping.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateBlockDeviceMappingList:
    import capo_ec2.types.launch_template_block_device_mapping

    out: LaunchTemplateBlockDeviceMappingList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.launch_template_block_device_mapping.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LaunchTemplateBlockDeviceMappingList:
    import capo_ec2.types.launch_template_block_device_mapping

    out: LaunchTemplateBlockDeviceMappingList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.launch_template_block_device_mapping.deserialize_ec2_query(
                child
            )
        )
    return out
