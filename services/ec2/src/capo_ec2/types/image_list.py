"""Generated from Smithy shape ``com.amazonaws.ec2#ImageList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image

ImageList: TypeAlias = list["capo_ec2.types.image.Image"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image

        capo_ec2.types.image.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> ImageList:
    import capo_ec2.types.image

    out: ImageList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.image.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ImageList:
    import capo_ec2.types.image

    out: ImageList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.image.deserialize_ec2_query(child))
    return out
