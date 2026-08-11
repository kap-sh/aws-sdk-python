"""Generated from Smithy shape ``com.amazonaws.rds#TagSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.tag_specification

TagSpecificationList: TypeAlias = list[
    "capo_rds.types.tag_specification.TagSpecification"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.tag_specification

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.tag_specification.serialize_query(
            item, pairs, f"{prefix}.item.{n}"
        )


def deserialize_query(el: Element) -> TagSpecificationList:
    import capo_rds.types.tag_specification

    out: TagSpecificationList = []
    for child in el.findall("item"):
        out.append(capo_rds.types.tag_specification.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TagSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.tag_specification

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.tag_specification.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TagSpecificationList:
    import capo_rds.types.tag_specification

    out: TagSpecificationList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.tag_specification.deserialize_query(child))
    return out
