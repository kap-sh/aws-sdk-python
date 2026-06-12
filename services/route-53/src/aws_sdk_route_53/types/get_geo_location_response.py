"""Generated from Smithy shape ``com.amazonaws.route53#GetGeoLocationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.geo_location_details


class GetGeoLocationResponse(TypedDict):
    geo_location_details: (
        "aws_sdk_route_53.types.geo_location_details.GeoLocationDetails"
    )
    """<p>A complex type that contains the codes and full continent, country, and subdivision names for the specified geolocation code.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetGeoLocationResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.geo_location_details

    aws_sdk_route_53.types.geo_location_details.serialize_xml(
        value["geo_location_details"], el, "GeoLocationDetails"
    )


def deserialize_xml(el: Element) -> GetGeoLocationResponse:
    out: GetGeoLocationResponse = {}  # type: ignore[typeddict-item]
    child_geo_location_details = el.find("GeoLocationDetails")
    if child_geo_location_details is not None:
        import aws_sdk_route_53.types.geo_location_details

        out["geo_location_details"] = (
            aws_sdk_route_53.types.geo_location_details.deserialize_xml(
                child_geo_location_details
            )
        )
    else:
        raise DeserializationError(
            "GetGeoLocationResponse.geo_location_details required"
        )
    return out
