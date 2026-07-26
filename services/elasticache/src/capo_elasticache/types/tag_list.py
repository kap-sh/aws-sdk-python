"""Generated from Smithy shape ``com.amazonaws.elasticache#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.tag

TagList: TypeAlias = list["capo_elasticache.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(value: TagList, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_elasticache.types.tag

    for n, item in enumerate(value, 1):
        capo_elasticache.types.tag.serialize_query(item, pairs, f"{prefix}.Tag.{n}")


def deserialize_query(el: Element) -> TagList:
    import capo_elasticache.types.tag

    out: TagList = []
    for child in el.findall("Tag"):
        out.append(capo_elasticache.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.tag

    for n, item in enumerate(value, 1):
        capo_elasticache.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TagList:
    import capo_elasticache.types.tag

    out: TagList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.tag.deserialize_query(child))
    return out
