"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAncestryEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_ancestry_entry

ImageAncestryEntryList: TypeAlias = list[
    "capo_ec2.types.image_ancestry_entry.ImageAncestryEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageAncestryEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_ancestry_entry

        capo_ec2.types.image_ancestry_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ImageAncestryEntryList:
    import capo_ec2.types.image_ancestry_entry

    out: ImageAncestryEntryList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.image_ancestry_entry.deserialize_ec2_query(child))
    return out
