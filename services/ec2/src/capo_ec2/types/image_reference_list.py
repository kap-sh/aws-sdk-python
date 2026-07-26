"""Generated from Smithy shape ``com.amazonaws.ec2#ImageReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_reference

ImageReferenceList: TypeAlias = list["capo_ec2.types.image_reference.ImageReference"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageReferenceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_reference

        capo_ec2.types.image_reference.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ImageReferenceList:
    import capo_ec2.types.image_reference

    out: ImageReferenceList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.image_reference.deserialize_ec2_query(child))
    return out
