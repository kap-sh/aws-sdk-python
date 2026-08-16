"""Generated from Smithy shape ``com.amazonaws.sns#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.tag

TagList: TypeAlias = list["capo_sns.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(value: TagList, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_sns.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.tag.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> TagList:
    import capo_sns.types.tag

    out: TagList = []
    for child in el.findall("member"):
        out.append(capo_sns.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TagList:
    import capo_sns.types.tag

    out: TagList = []
    for child in parent.findall(tag):
        out.append(capo_sns.types.tag.deserialize_query(child))
    return out
