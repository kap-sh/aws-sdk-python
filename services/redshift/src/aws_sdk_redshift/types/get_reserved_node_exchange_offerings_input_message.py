"""Generated from Smithy shape ``com.amazonaws.redshift#GetReservedNodeExchangeOfferingsInputMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class GetReservedNodeExchangeOfferingsInputMessage(TypedDict):
    reserved_node_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A string representing the node identifier for the DC1 Reserved Node to be exchanged.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>An integer setting the maximum number of ReservedNodeOfferings to retrieve.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of ReservedNodeOfferings.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetReservedNodeExchangeOfferingsInputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_node_id" in value:
        pairs.append((f"{prefix}.ReservedNodeId", str(value["reserved_node_id"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> GetReservedNodeExchangeOfferingsInputMessage:
    out: GetReservedNodeExchangeOfferingsInputMessage = {}  # type: ignore[typeddict-item]
    child_reserved_node_id = el.find("ReservedNodeId")
    if child_reserved_node_id is not None:
        out["reserved_node_id"] = str(child_reserved_node_id.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
