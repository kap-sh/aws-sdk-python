"""Generated from Smithy shape ``com.amazonaws.route53#ListGeoLocationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.geo_location_continent_code
    import aws_sdk_route_53.types.geo_location_country_code
    import aws_sdk_route_53.types.geo_location_subdivision_code


class ListGeoLocationsRequest(TypedDict, closed=True):
    start_continent_code: NotRequired[
        "aws_sdk_route_53.types.geo_location_continent_code.GeoLocationContinentCode"
    ]
    """<p>The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is true, and if <code>NextContinentCode</code> from the previous response has a value, enter that value in <code>startcontinentcode</code> to return the next page of results.</p> <p>Include <code>startcontinentcode</code> only if you want to list continents. Don't include <code>startcontinentcode</code> when you're listing countries or countries with their subdivisions.</p>"""
    start_country_code: NotRequired[
        "aws_sdk_route_53.types.geo_location_country_code.GeoLocationCountryCode"
    ]
    """<p>The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is <code>true</code>, and if <code>NextCountryCode</code> from the previous response has a value, enter that value in <code>startcountrycode</code> to return the next page of results.</p>"""
    start_subdivision_code: NotRequired[
        "aws_sdk_route_53.types.geo_location_subdivision_code.GeoLocationSubdivisionCode"
    ]
    """<p>The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is <code>true</code>, and if <code>NextSubdivisionCode</code> from the previous response has a value, enter that value in <code>startsubdivisioncode</code> to return the next page of results.</p> <p>To list subdivisions (U.S. states), you must include both <code>startcountrycode</code> and <code>startsubdivisioncode</code>.</p>"""
    max_items: NotRequired["int"]
    """<p>(Optional) The maximum number of geolocations to be included in the response body for this request. If more than <code>maxitems</code> geolocations remain to be listed, then the value of the <code>IsTruncated</code> element in the response is <code>true</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListGeoLocationsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListGeoLocationsRequest:
    out: ListGeoLocationsRequest = {}  # type: ignore[typeddict-item]
    return out
