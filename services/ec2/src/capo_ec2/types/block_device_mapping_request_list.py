"""Generated from Smithy shape ``com.amazonaws.ec2#BlockDeviceMappingRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.block_device_mapping

BlockDeviceMappingRequestList: TypeAlias = list[
    "capo_ec2.types.block_device_mapping.BlockDeviceMapping"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BlockDeviceMappingRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.block_device_mapping

        capo_ec2.types.block_device_mapping.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> BlockDeviceMappingRequestList:
    import capo_ec2.types.block_device_mapping

    out: BlockDeviceMappingRequestList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.block_device_mapping.deserialize_ec2_query(child))
    return out
