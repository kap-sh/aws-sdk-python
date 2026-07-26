"""Generated from Smithy shape ``com.amazonaws.sts#tagKeyListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.tag_key_type

tagKeyListType: TypeAlias = list["capo_sts.types.tag_key_type.tagKeyType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: tagKeyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> tagKeyListType:
    out: tagKeyListType = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: tagKeyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> tagKeyListType:
    out: tagKeyListType = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
