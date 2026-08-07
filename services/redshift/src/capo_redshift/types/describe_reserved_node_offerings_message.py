"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeReservedNodeOfferingsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DescribeReservedNodeOfferingsMessage(TypedDict, closed=True):
    reserved_node_offering_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier for the offering.</p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeReservedNodeOfferings</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReservedNodeOfferingsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedNodeOfferingId",
                str(value["reserved_node_offering_id"]),
            )
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeReservedNodeOfferingsMessage:
    out: DescribeReservedNodeOfferingsMessage = {}  # type: ignore[typeddict-item]
    child_reserved_node_offering_id = el.find("ReservedNodeOfferingId")
    if child_reserved_node_offering_id is not None:
        out["reserved_node_offering_id"] = str(
            child_reserved_node_offering_id.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
