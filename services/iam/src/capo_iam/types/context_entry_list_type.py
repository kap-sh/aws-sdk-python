"""Generated from Smithy shape ``com.amazonaws.iam#ContextEntryListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.context_entry

ContextEntryListType: TypeAlias = list["capo_iam.types.context_entry.ContextEntry"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ContextEntryListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.context_entry

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.context_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ContextEntryListType:
    import capo_iam.types.context_entry

    out: ContextEntryListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.context_entry.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ContextEntryListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.context_entry

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.context_entry.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ContextEntryListType:
    import capo_iam.types.context_entry

    out: ContextEntryListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.context_entry.deserialize_query(child))
    return out
