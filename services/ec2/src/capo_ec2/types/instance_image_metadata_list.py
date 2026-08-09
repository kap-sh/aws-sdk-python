"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceImageMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_image_metadata

InstanceImageMetadataList: TypeAlias = list[
    "capo_ec2.types.instance_image_metadata.InstanceImageMetadata"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceImageMetadataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_image_metadata

        capo_ec2.types.instance_image_metadata.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceImageMetadataList:
    import capo_ec2.types.instance_image_metadata

    out: InstanceImageMetadataList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_image_metadata.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceImageMetadataList:
    import capo_ec2.types.instance_image_metadata

    out: InstanceImageMetadataList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_image_metadata.deserialize_ec2_query(child))
    return out
