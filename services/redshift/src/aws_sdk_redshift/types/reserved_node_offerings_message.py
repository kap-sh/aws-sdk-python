"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeOfferingsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.reserved_node_offering_list
    import aws_sdk_redshift.types.string


class ReservedNodeOfferingsMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    reserved_node_offerings: NotRequired[
        "aws_sdk_redshift.types.reserved_node_offering_list.ReservedNodeOfferingList"
    ]
    """<p>A list of <code>ReservedNodeOffering</code> objects.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeOfferingsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "reserved_node_offerings" in value:
        import aws_sdk_redshift.types.reserved_node_offering_list

        aws_sdk_redshift.types.reserved_node_offering_list.serialize_query(
            value["reserved_node_offerings"], pairs, f"{prefix}.ReservedNodeOfferings"
        )


def deserialize_query(el: Element) -> ReservedNodeOfferingsMessage:
    out: ReservedNodeOfferingsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_node_offerings = el.find("ReservedNodeOfferings")
    if child_reserved_node_offerings is not None:
        import aws_sdk_redshift.types.reserved_node_offering_list

        out["reserved_node_offerings"] = (
            aws_sdk_redshift.types.reserved_node_offering_list.deserialize_query(
                child_reserved_node_offerings
            )
        )
    return out
