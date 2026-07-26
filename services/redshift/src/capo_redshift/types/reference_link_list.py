"""Generated from Smithy shape ``com.amazonaws.redshift#ReferenceLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reference_link

ReferenceLinkList: TypeAlias = list["capo_redshift.types.reference_link.ReferenceLink"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReferenceLinkList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.reference_link

    for n, item in enumerate(value, 1):
        capo_redshift.types.reference_link.serialize_query(
            item, pairs, f"{prefix}.ReferenceLink.{n}"
        )


def deserialize_query(el: Element) -> ReferenceLinkList:
    import capo_redshift.types.reference_link

    out: ReferenceLinkList = []
    for child in el.findall("ReferenceLink"):
        out.append(capo_redshift.types.reference_link.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReferenceLinkList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.reference_link

    for n, item in enumerate(value, 1):
        capo_redshift.types.reference_link.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ReferenceLinkList:
    import capo_redshift.types.reference_link

    out: ReferenceLinkList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.reference_link.deserialize_query(child))
    return out
