"""Generated from Smithy shape ``com.amazonaws.sts#tagListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.tag

tagListType: TypeAlias = list["capo_sts.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(
    value: tagListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sts.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sts.types.tag.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> tagListType:
    import capo_sts.types.tag

    out: tagListType = []
    for child in el.findall("member"):
        out.append(capo_sts.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: tagListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sts.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sts.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> tagListType:
    import capo_sts.types.tag

    out: tagListType = []
    for child in parent.findall(tag):
        out.append(capo_sts.types.tag.deserialize_query(child))
    return out
