"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reserved_node_offering

ReservedNodeOfferingList: TypeAlias = list[
    "capo_redshift.types.reserved_node_offering.ReservedNodeOffering"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeOfferingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.reserved_node_offering

    for n, item in enumerate(value, 1):
        capo_redshift.types.reserved_node_offering.serialize_query(
            item, pairs, f"{prefix}.ReservedNodeOffering.{n}"
        )


def deserialize_query(el: Element) -> ReservedNodeOfferingList:
    import capo_redshift.types.reserved_node_offering

    out: ReservedNodeOfferingList = []
    for child in el.findall("ReservedNodeOffering"):
        out.append(capo_redshift.types.reserved_node_offering.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReservedNodeOfferingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.reserved_node_offering

    for n, item in enumerate(value, 1):
        capo_redshift.types.reserved_node_offering.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReservedNodeOfferingList:
    import capo_redshift.types.reserved_node_offering

    out: ReservedNodeOfferingList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.reserved_node_offering.deserialize_query(child))
    return out
