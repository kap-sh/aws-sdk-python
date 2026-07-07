"""Generated from Smithy shape ``com.amazonaws.redshift#PurchaseReservedNodeOfferingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class PurchaseReservedNodeOfferingMessage(TypedDict, closed=True):
    reserved_node_offering_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier of the reserved node offering you want to purchase.</p>"""
    node_count: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The number of reserved nodes that you want to purchase.</p> <p>Default: <code>1</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PurchaseReservedNodeOfferingMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedNodeOfferingId",
                str(value["reserved_node_offering_id"]),
            )
        )
    if "node_count" in value:
        pairs.append((f"{prefix}.NodeCount", str(value["node_count"])))


def deserialize_query(el: Element) -> PurchaseReservedNodeOfferingMessage:
    out: PurchaseReservedNodeOfferingMessage = {}  # type: ignore[typeddict-item]
    child_reserved_node_offering_id = el.find("ReservedNodeOfferingId")
    if child_reserved_node_offering_id is not None:
        out["reserved_node_offering_id"] = str(
            child_reserved_node_offering_id.text or ""
        )
    child_node_count = el.find("NodeCount")
    if child_node_count is not None:
        out["node_count"] = int(child_node_count.text or "")
    return out
