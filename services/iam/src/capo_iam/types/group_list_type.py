"""Generated from Smithy shape ``com.amazonaws.iam#groupListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.group

groupListType: TypeAlias = list["capo_iam.types.group.Group"]


# --- awsQuery ser/de ---
def serialize_query(
    value: groupListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.group.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> groupListType:
    import capo_iam.types.group

    out: groupListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: groupListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> groupListType:
    import capo_iam.types.group

    out: groupListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.group.deserialize_query(child))
    return out
