"""Generated from Smithy shape ``com.amazonaws.iam#tagListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.tag

tagListType: TypeAlias = list["capo_iam.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(
    value: tagListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.tag.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> tagListType:
    import capo_iam.types.tag

    out: tagListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: tagListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.tag

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> tagListType:
    import capo_iam.types.tag

    out: tagListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.tag.deserialize_query(child))
    return out
