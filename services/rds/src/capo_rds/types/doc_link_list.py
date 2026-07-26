"""Generated from Smithy shape ``com.amazonaws.rds#DocLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.doc_link

DocLinkList: TypeAlias = list["capo_rds.types.doc_link.DocLink"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DocLinkList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.doc_link

    for n, item in enumerate(value, 1):
        capo_rds.types.doc_link.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> DocLinkList:
    import capo_rds.types.doc_link

    out: DocLinkList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.doc_link.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DocLinkList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.doc_link

    for n, item in enumerate(value, 1):
        capo_rds.types.doc_link.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DocLinkList:
    import capo_rds.types.doc_link

    out: DocLinkList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.doc_link.deserialize_query(child))
    return out
