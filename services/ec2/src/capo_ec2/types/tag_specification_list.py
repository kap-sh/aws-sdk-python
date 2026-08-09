"""Generated from Smithy shape ``com.amazonaws.ec2#TagSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.tag_specification

TagSpecificationList: TypeAlias = list[
    "capo_ec2.types.tag_specification.TagSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.tag_specification

        capo_ec2.types.tag_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TagSpecificationList:
    import capo_ec2.types.tag_specification

    out: TagSpecificationList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.tag_specification.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TagSpecificationList:
    import capo_ec2.types.tag_specification

    out: TagSpecificationList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.tag_specification.deserialize_ec2_query(child))
    return out
