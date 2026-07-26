"""Generated from Smithy shape ``com.amazonaws.autoscaling#BlockDeviceMappings``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.block_device_mapping

BlockDeviceMappings: TypeAlias = list[
    "capo_auto_scaling.types.block_device_mapping.BlockDeviceMapping"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BlockDeviceMappings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.block_device_mapping

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.block_device_mapping.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BlockDeviceMappings:
    import capo_auto_scaling.types.block_device_mapping

    out: BlockDeviceMappings = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.block_device_mapping.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: BlockDeviceMappings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.block_device_mapping

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.block_device_mapping.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BlockDeviceMappings:
    import capo_auto_scaling.types.block_device_mapping

    out: BlockDeviceMappings = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.block_device_mapping.deserialize_query(child)
        )
    return out
