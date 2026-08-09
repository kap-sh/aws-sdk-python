"""Generated from Smithy shape ``com.amazonaws.ec2#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.tag

TagList: TypeAlias = list["capo_ec2.types.tag.Tag"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.tag

        capo_ec2.types.tag.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> TagList:
    import capo_ec2.types.tag

    out: TagList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.tag.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TagList:
    import capo_ec2.types.tag

    out: TagList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.tag.deserialize_ec2_query(child))
    return out
