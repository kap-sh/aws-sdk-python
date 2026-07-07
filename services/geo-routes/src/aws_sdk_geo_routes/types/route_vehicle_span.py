"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleSpan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.country_code3
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.index_list
    import aws_sdk_geo_routes.types.localized_string_list
    import aws_sdk_geo_routes.types.route_number_list
    import aws_sdk_geo_routes.types.route_span_car_access_attribute_list
    import aws_sdk_geo_routes.types.route_span_dynamic_speed_details
    import aws_sdk_geo_routes.types.route_span_gate_attribute
    import aws_sdk_geo_routes.types.route_span_railway_crossing_attribute
    import aws_sdk_geo_routes.types.route_span_road_attribute_list
    import aws_sdk_geo_routes.types.route_span_scooter_access_attribute_list
    import aws_sdk_geo_routes.types.route_span_speed_limit_details
    import aws_sdk_geo_routes.types.route_span_truck_access_attribute_list
    import aws_sdk_geo_routes.types.sensitive_integer
    import aws_sdk_geo_routes.types.sensitive_string


class RouteVehicleSpan(TypedDict, closed=True):
    best_case_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span without traffic congestion.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    car_access: NotRequired[
        "aws_sdk_geo_routes.types.route_span_car_access_attribute_list.RouteSpanCarAccessAttributeList"
    ]
    """<p>Access attributes for a car corresponding to the span.</p>"""
    country: NotRequired["aws_sdk_geo_routes.types.country_code3.CountryCode3"]
    """<p>3 letter Country code corresponding to the Span.</p>"""
    distance: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    dynamic_speed: NotRequired[
        "aws_sdk_geo_routes.types.route_span_dynamic_speed_details.RouteSpanDynamicSpeedDetails"
    ]
    """<p>Dynamic speed details corresponding to the span.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    functional_classification: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>A numerical value indicating the functional classification of the road segment corresponding to the span.</p> <p>Classification values are part of the hierarchical network that helps determine a logical and efficient route, and have the following definitions:</p> <ol> <li> <p>Roads that allow for high volume, maximum speed traffic movement between and through major metropolitan areas.</p> </li> <li> <p>Roads that are used to channel traffic to functional class 1 roads for travel between and through cities in the shortest amount of time.</p> </li> <li> <p>Roads that intersect functional class 2 roads and provide a high volume of traffic movement at a lower level of mobility than functional class 2 roads.</p> </li> <li> <p>Roads that provide for a high volume of traffic movement at moderate speeds between neighborhoods.</p> </li> <li> <p>Roads with volume and traffic movement below the level of any other functional class.</p> </li> </ol>"""
    gate: NotRequired[
        "aws_sdk_geo_routes.types.route_span_gate_attribute.RouteSpanGateAttribute"
    ]
    """<p>Attributes corresponding to a gate. The gate is present at the end of the returned span.</p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this span.</p>"""
    incidents: NotRequired["aws_sdk_geo_routes.types.index_list.IndexList"]
    """<p>Incidents corresponding to the span. These index into the Incidents in the parent Leg.</p>"""
    names: NotRequired[
        "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    ]
    """<p>Provides an array of names of the vehicle span in available languages.</p>"""
    notices: NotRequired["aws_sdk_geo_routes.types.index_list.IndexList"]
    """<p>Notices are additional information returned that indicate issues that occurred during route calculation.</p>"""
    railway_crossing: NotRequired[
        "aws_sdk_geo_routes.types.route_span_railway_crossing_attribute.RouteSpanRailwayCrossingAttribute"
    ]
    """<p>Attributes corresponding to a railway crossing. The gate is present at the end of the returned span.</p>"""
    region: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>2-3 letter Region code corresponding to the Span. This is either a province or a state.</p>"""
    road_attributes: NotRequired[
        "aws_sdk_geo_routes.types.route_span_road_attribute_list.RouteSpanRoadAttributeList"
    ]
    """<p>Attributes for the road segment corresponding to the span. </p>"""
    route_numbers: NotRequired[
        "aws_sdk_geo_routes.types.route_number_list.RouteNumberList"
    ]
    """<p>Designated route name or number corresponding to the span.</p>"""
    scooter_access: NotRequired[
        "aws_sdk_geo_routes.types.route_span_scooter_access_attribute_list.RouteSpanScooterAccessAttributeList"
    ]
    """<p>Access attributes for a scooter corresponding to the span.</p>"""
    speed_limit: NotRequired[
        "aws_sdk_geo_routes.types.route_span_speed_limit_details.RouteSpanSpeedLimitDetails"
    ]
    """<p>Speed limit details corresponding to the span.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    toll_systems: NotRequired["aws_sdk_geo_routes.types.index_list.IndexList"]
    """<p>Toll systems are authorities that collect payments for the toll.</p>"""
    truck_access: NotRequired[
        "aws_sdk_geo_routes.types.route_span_truck_access_attribute_list.RouteSpanTruckAccessAttributeList"
    ]
    """<p>Access attributes for a truck corresponding to the span.</p>"""
    truck_road_types: NotRequired["aws_sdk_geo_routes.types.index_list.IndexList"]
    """<p>Truck road type identifiers. <code>BK1</code> through <code>BK4</code> apply only to Sweden. <code>A2,A4,B2,B4,C,D,ET2,ET4</code> apply only to Mexico.</p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    typical_duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span under typical traffic congestion. </p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    zones: NotRequired["aws_sdk_geo_routes.types.index_list.IndexList"]
    """<p>Zones corresponding to this leg of the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleSpan) -> dict:
    out: dict = {}
    out["BestCaseDuration"] = value.get("best_case_duration", 0)
    if "car_access" in value:
        import aws_sdk_geo_routes.types.route_span_car_access_attribute_list

        out["CarAccess"] = (
            aws_sdk_geo_routes.types.route_span_car_access_attribute_list.serialize_json(
                value["car_access"]
            )
        )
    if "country" in value:
        out["Country"] = value["country"]
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "dynamic_speed" in value:
        import aws_sdk_geo_routes.types.route_span_dynamic_speed_details

        out["DynamicSpeed"] = (
            aws_sdk_geo_routes.types.route_span_dynamic_speed_details.serialize_json(
                value["dynamic_speed"]
            )
        )
    if "functional_classification" in value:
        out["FunctionalClassification"] = value["functional_classification"]
    if "gate" in value:
        import aws_sdk_geo_routes.types.route_span_gate_attribute

        out["Gate"] = aws_sdk_geo_routes.types.route_span_gate_attribute.serialize_json(
            value["gate"]
        )
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "incidents" in value:
        import aws_sdk_geo_routes.types.index_list

        out["Incidents"] = aws_sdk_geo_routes.types.index_list.serialize_json(
            value["incidents"]
        )
    if "names" in value:
        import aws_sdk_geo_routes.types.localized_string_list

        out["Names"] = aws_sdk_geo_routes.types.localized_string_list.serialize_json(
            value["names"]
        )
    if "notices" in value:
        import aws_sdk_geo_routes.types.index_list

        out["Notices"] = aws_sdk_geo_routes.types.index_list.serialize_json(
            value["notices"]
        )
    if "railway_crossing" in value:
        import aws_sdk_geo_routes.types.route_span_railway_crossing_attribute

        out["RailwayCrossing"] = (
            aws_sdk_geo_routes.types.route_span_railway_crossing_attribute.serialize_json(
                value["railway_crossing"]
            )
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "road_attributes" in value:
        import aws_sdk_geo_routes.types.route_span_road_attribute_list

        out["RoadAttributes"] = (
            aws_sdk_geo_routes.types.route_span_road_attribute_list.serialize_json(
                value["road_attributes"]
            )
        )
    if "route_numbers" in value:
        import aws_sdk_geo_routes.types.route_number_list

        out["RouteNumbers"] = aws_sdk_geo_routes.types.route_number_list.serialize_json(
            value["route_numbers"]
        )
    if "scooter_access" in value:
        import aws_sdk_geo_routes.types.route_span_scooter_access_attribute_list

        out["ScooterAccess"] = (
            aws_sdk_geo_routes.types.route_span_scooter_access_attribute_list.serialize_json(
                value["scooter_access"]
            )
        )
    if "speed_limit" in value:
        import aws_sdk_geo_routes.types.route_span_speed_limit_details

        out["SpeedLimit"] = (
            aws_sdk_geo_routes.types.route_span_speed_limit_details.serialize_json(
                value["speed_limit"]
            )
        )
    if "toll_systems" in value:
        import aws_sdk_geo_routes.types.index_list

        out["TollSystems"] = aws_sdk_geo_routes.types.index_list.serialize_json(
            value["toll_systems"]
        )
    if "truck_access" in value:
        import aws_sdk_geo_routes.types.route_span_truck_access_attribute_list

        out["TruckAccess"] = (
            aws_sdk_geo_routes.types.route_span_truck_access_attribute_list.serialize_json(
                value["truck_access"]
            )
        )
    if "truck_road_types" in value:
        import aws_sdk_geo_routes.types.index_list

        out["TruckRoadTypes"] = aws_sdk_geo_routes.types.index_list.serialize_json(
            value["truck_road_types"]
        )
    out["TypicalDuration"] = value.get("typical_duration", 0)
    if "zones" in value:
        import aws_sdk_geo_routes.types.index_list

        out["Zones"] = aws_sdk_geo_routes.types.index_list.serialize_json(
            value["zones"]
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleSpan:
    out: RouteVehicleSpan = {}  # type: ignore[typeddict-item]
    if "BestCaseDuration" in data:
        out["best_case_duration"] = data["BestCaseDuration"]
    else:
        out["best_case_duration"] = 0
    if "CarAccess" in data:
        import aws_sdk_geo_routes.types.route_span_car_access_attribute_list

        out["car_access"] = (
            aws_sdk_geo_routes.types.route_span_car_access_attribute_list.deserialize_json(
                data["CarAccess"]
            )
        )
    if "Country" in data:
        out["country"] = data["Country"]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "DynamicSpeed" in data:
        import aws_sdk_geo_routes.types.route_span_dynamic_speed_details

        out["dynamic_speed"] = (
            aws_sdk_geo_routes.types.route_span_dynamic_speed_details.deserialize_json(
                data["DynamicSpeed"]
            )
        )
    if "FunctionalClassification" in data:
        out["functional_classification"] = data["FunctionalClassification"]
    if "Gate" in data:
        import aws_sdk_geo_routes.types.route_span_gate_attribute

        out["gate"] = (
            aws_sdk_geo_routes.types.route_span_gate_attribute.deserialize_json(
                data["Gate"]
            )
        )
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    if "Incidents" in data:
        import aws_sdk_geo_routes.types.index_list

        out["incidents"] = aws_sdk_geo_routes.types.index_list.deserialize_json(
            data["Incidents"]
        )
    if "Names" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["names"] = aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
            data["Names"]
        )
    if "Notices" in data:
        import aws_sdk_geo_routes.types.index_list

        out["notices"] = aws_sdk_geo_routes.types.index_list.deserialize_json(
            data["Notices"]
        )
    if "RailwayCrossing" in data:
        import aws_sdk_geo_routes.types.route_span_railway_crossing_attribute

        out["railway_crossing"] = (
            aws_sdk_geo_routes.types.route_span_railway_crossing_attribute.deserialize_json(
                data["RailwayCrossing"]
            )
        )
    if "Region" in data:
        out["region"] = data["Region"]
    if "RoadAttributes" in data:
        import aws_sdk_geo_routes.types.route_span_road_attribute_list

        out["road_attributes"] = (
            aws_sdk_geo_routes.types.route_span_road_attribute_list.deserialize_json(
                data["RoadAttributes"]
            )
        )
    if "RouteNumbers" in data:
        import aws_sdk_geo_routes.types.route_number_list

        out["route_numbers"] = (
            aws_sdk_geo_routes.types.route_number_list.deserialize_json(
                data["RouteNumbers"]
            )
        )
    if "ScooterAccess" in data:
        import aws_sdk_geo_routes.types.route_span_scooter_access_attribute_list

        out["scooter_access"] = (
            aws_sdk_geo_routes.types.route_span_scooter_access_attribute_list.deserialize_json(
                data["ScooterAccess"]
            )
        )
    if "SpeedLimit" in data:
        import aws_sdk_geo_routes.types.route_span_speed_limit_details

        out["speed_limit"] = (
            aws_sdk_geo_routes.types.route_span_speed_limit_details.deserialize_json(
                data["SpeedLimit"]
            )
        )
    if "TollSystems" in data:
        import aws_sdk_geo_routes.types.index_list

        out["toll_systems"] = aws_sdk_geo_routes.types.index_list.deserialize_json(
            data["TollSystems"]
        )
    if "TruckAccess" in data:
        import aws_sdk_geo_routes.types.route_span_truck_access_attribute_list

        out["truck_access"] = (
            aws_sdk_geo_routes.types.route_span_truck_access_attribute_list.deserialize_json(
                data["TruckAccess"]
            )
        )
    if "TruckRoadTypes" in data:
        import aws_sdk_geo_routes.types.index_list

        out["truck_road_types"] = aws_sdk_geo_routes.types.index_list.deserialize_json(
            data["TruckRoadTypes"]
        )
    if "TypicalDuration" in data:
        out["typical_duration"] = data["TypicalDuration"]
    else:
        out["typical_duration"] = 0
    if "Zones" in data:
        import aws_sdk_geo_routes.types.index_list

        out["zones"] = aws_sdk_geo_routes.types.index_list.deserialize_json(
            data["Zones"]
        )
    return out
