"""Generated from Smithy shape ``com.amazonaws.route53#ListCidrLocationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.location_summaries
    import capo_route_53.types.pagination_token


class ListCidrLocationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>An opaque pagination token to indicate where the service is to begin enumerating results.</p> <p>If no value is provided, the listing of results starts from the beginning.</p>"""
    cidr_locations: NotRequired[
        "capo_route_53.types.location_summaries.LocationSummaries"
    ]
    """<p>A complex type that contains information about the list of CIDR locations.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListCidrLocationsResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "cidr_locations" in value:
        import capo_route_53.types.location_summaries

        capo_route_53.types.location_summaries.serialize_xml(
            value["cidr_locations"], el, "CidrLocations"
        )


def deserialize_xml(el: Element) -> ListCidrLocationsResponse:
    out: ListCidrLocationsResponse = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_cidr_locations = el.find("CidrLocations")
    if child_cidr_locations is not None:
        import capo_route_53.types.location_summaries

        out["cidr_locations"] = capo_route_53.types.location_summaries.deserialize_xml(
            child_cidr_locations
        )
    return out
