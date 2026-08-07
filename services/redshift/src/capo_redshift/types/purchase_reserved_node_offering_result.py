"""Generated from Smithy shape ``com.amazonaws.redshift#PurchaseReservedNodeOfferingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reserved_node


class PurchaseReservedNodeOfferingResult(TypedDict, closed=True):
    reserved_node: NotRequired["capo_redshift.types.reserved_node.ReservedNode"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PurchaseReservedNodeOfferingResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_node" in value:
        import capo_redshift.types.reserved_node

        capo_redshift.types.reserved_node.serialize_query(
            value["reserved_node"], pairs, f"{key_prefix}ReservedNode"
        )


def deserialize_query(el: Element) -> PurchaseReservedNodeOfferingResult:
    out: PurchaseReservedNodeOfferingResult = {}  # type: ignore[typeddict-item]
    child_reserved_node = el.find("ReservedNode")
    if child_reserved_node is not None:
        import capo_redshift.types.reserved_node

        out["reserved_node"] = capo_redshift.types.reserved_node.deserialize_query(
            child_reserved_node
        )
    return out
