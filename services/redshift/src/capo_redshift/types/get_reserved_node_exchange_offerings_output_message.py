"""Generated from Smithy shape ``com.amazonaws.redshift#GetReservedNodeExchangeOfferingsOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reserved_node_offering_list
    import capo_redshift.types.string


class GetReservedNodeExchangeOfferingsOutputMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point for returning a set of response records. When the results of a <code>GetReservedNodeExchangeOfferings</code> request exceed the value specified in MaxRecords, Amazon Redshift returns a value in the marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the marker parameter and retrying the request. </p>"""
    reserved_node_offerings: NotRequired[
        "capo_redshift.types.reserved_node_offering_list.ReservedNodeOfferingList"
    ]
    """<p>Returns an array of <a>ReservedNodeOffering</a> objects.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetReservedNodeExchangeOfferingsOutputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "reserved_node_offerings" in value:
        import capo_redshift.types.reserved_node_offering_list

        capo_redshift.types.reserved_node_offering_list.serialize_query(
            value["reserved_node_offerings"], pairs, f"{prefix}.ReservedNodeOfferings"
        )


def deserialize_query(el: Element) -> GetReservedNodeExchangeOfferingsOutputMessage:
    out: GetReservedNodeExchangeOfferingsOutputMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_node_offerings = el.find("ReservedNodeOfferings")
    if child_reserved_node_offerings is not None:
        import capo_redshift.types.reserved_node_offering_list

        out["reserved_node_offerings"] = (
            capo_redshift.types.reserved_node_offering_list.deserialize_query(
                child_reserved_node_offerings
            )
        )
    return out
