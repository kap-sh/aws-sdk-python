"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.tag

TagList: TypeAlias = list["capo_elastic_load_balancing.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(value: TagList, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_elastic_load_balancing.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.tag.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TagList:
    import capo_elastic_load_balancing.types.tag

    out: TagList = []
    for child in el.findall("member"):
        out.append(capo_elastic_load_balancing.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.tag.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TagList:
    import capo_elastic_load_balancing.types.tag

    out: TagList = []
    for child in parent.findall(tag):
        out.append(capo_elastic_load_balancing.types.tag.deserialize_query(child))
    return out
