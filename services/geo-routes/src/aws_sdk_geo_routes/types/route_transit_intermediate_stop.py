"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStop``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_transit_departure
    import aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute_list
    import aws_sdk_geo_routes.types.route_transit_transport_mode_details


class RouteTransitIntermediateStop(TypedDict, closed=True):
    attributes: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute_list.RouteTransitIntermediateStopAttributeList"
    ]
    """<p>Attributes of the intermediate stop.</p>"""
    departure: "aws_sdk_geo_routes.types.route_transit_departure.RouteTransitDeparture"
    """<p>Departure details for the intermediate stop.</p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the stop.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this stop.</p>"""
    transport: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_transport_mode_details.RouteTransitTransportModeDetails"
    ]
    """<p>Transport mode details at the intermediate stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIntermediateStop) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute_list

        out["Attributes"] = (
            aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute_list.serialize_json(
                value["attributes"]
            )
        )
    import aws_sdk_geo_routes.types.route_transit_departure

    out["Departure"] = aws_sdk_geo_routes.types.route_transit_departure.serialize_json(
        value["departure"]
    )
    out["Duration"] = value["duration"]
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "transport" in value:
        import aws_sdk_geo_routes.types.route_transit_transport_mode_details

        out["Transport"] = (
            aws_sdk_geo_routes.types.route_transit_transport_mode_details.serialize_json(
                value["transport"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTransitIntermediateStop:
    out: RouteTransitIntermediateStop = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute_list

        out["attributes"] = (
            aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    if "Departure" in data:
        import aws_sdk_geo_routes.types.route_transit_departure

        out["departure"] = (
            aws_sdk_geo_routes.types.route_transit_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteTransitIntermediateStop.departure required")
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTransitIntermediateStop.duration required")
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    if "Transport" in data:
        import aws_sdk_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            aws_sdk_geo_routes.types.route_transit_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    return out
