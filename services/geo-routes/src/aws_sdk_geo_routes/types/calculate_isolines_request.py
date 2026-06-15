"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateIsolinesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.api_key
    import aws_sdk_geo_routes.types.geometry_format
    import aws_sdk_geo_routes.types.isoline_allow_options
    import aws_sdk_geo_routes.types.isoline_avoidance_options
    import aws_sdk_geo_routes.types.isoline_destination_options
    import aws_sdk_geo_routes.types.isoline_granularity_options
    import aws_sdk_geo_routes.types.isoline_optimization_objective
    import aws_sdk_geo_routes.types.isoline_origin_options
    import aws_sdk_geo_routes.types.isoline_thresholds
    import aws_sdk_geo_routes.types.isoline_traffic_options
    import aws_sdk_geo_routes.types.isoline_travel_mode
    import aws_sdk_geo_routes.types.isoline_travel_mode_options
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.routing_objective
    import aws_sdk_geo_routes.types.sensitive_boolean
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset


class CalculateIsolinesRequest(TypedDict):
    allow: NotRequired[
        "aws_sdk_geo_routes.types.isoline_allow_options.IsolineAllowOptions"
    ]
    """<p>Enables special road types or features that should be considered for routing even if they might be restricted by default for the selected travel mode. These include high-occupancy vehicle and toll lanes.</p>"""
    arrival_time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Determine areas from which <code>Destination</code> can be reached by this time, taking into account predicted traffic conditions and working backward to account for congestion patterns. This attribute cannot be used together with <code>DepartureTime</code> or <code>DepartNow</code>. Specified as an ISO-8601 timestamp with timezone offset.</p> <p>Time format: <code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    avoid: NotRequired[
        "aws_sdk_geo_routes.types.isoline_avoidance_options.IsolineAvoidanceOptions"
    ]
    """<p>Specifies road types, features, or areas to avoid (if possible) when calculating reachable areas. These are treated as preferences rather than strict constraints—if a route cannot be calculated without using an avoided feature, that avoidance preference may be ignored.</p>"""
    depart_now: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>When true, uses the current time as the departure time and takes current traffic conditions into account. This attribute cannot be used together with <code>DepartureTime</code> or <code>ArrivalTime</code>.</p>"""
    departure_time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Determine areas that can be reached when departing at this time, taking into account predicted traffic conditions. This attribute cannot be used together with <code>ArrivalTime</code> or <code>DepartNow</code>. Specified as an ISO-8601 timestamp with timezone offset.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    destination: NotRequired["aws_sdk_geo_routes.types.position.Position"]
    """<p>An optional destination point, specified as <code>[longitude, latitude]</code> coordinates. When provided, the service calculates areas from which this destination can be reached within the specified thresholds. This reverses the usual isoline calculation to show areas that could reach your location, rather than areas you could reach from your location. Either <code>Origin</code> or <code>Destination</code> must be provided.</p>"""
    destination_options: NotRequired[
        "aws_sdk_geo_routes.types.isoline_destination_options.IsolineDestinationOptions"
    ]
    """<p>Options that control how the destination point is matched to the road network and how routes can approach it. These options help improve travel time accuracy by accounting for real-world access to the destination.</p>"""
    isoline_geometry_format: NotRequired[
        "aws_sdk_geo_routes.types.geometry_format.GeometryFormat"
    ]
    """<p>The format of the returned IsolineGeometry. </p> <p>Default value:<code>FlexiblePolyline</code> </p>"""
    isoline_granularity: NotRequired[
        "aws_sdk_geo_routes.types.isoline_granularity_options.IsolineGranularityOptions"
    ]
    """<p>Controls the detail level of the generated isolines. Higher granularity produces smoother shapes but requires more processing time and results in larger responses.</p>"""
    key: NotRequired["aws_sdk_geo_routes.types.api_key.ApiKey"]
    """<p>An Amazon Location Service API Key with access to this action. If omitted, the request must be signed using Signature Version 4.</p>"""
    optimize_isoline_for: NotRequired[
        "aws_sdk_geo_routes.types.isoline_optimization_objective.IsolineOptimizationObjective"
    ]
    """<p>Controls the trade-off between calculation speed and isoline precision. Choose <code> FastCalculation</code> for quicker results with less detail, <code>AccurateCalculation</code> for more precise results, or <code>BalancedCalculation</code> for a middle ground.</p> <p>Default value: <code>BalancedCalculation</code> </p>"""
    optimize_routing_for: NotRequired[
        "aws_sdk_geo_routes.types.routing_objective.RoutingObjective"
    ]
    """<p>Determines whether routes prioritize shortest travel time (<code>FastestRoute</code>) or shortest physical distance (<code>ShortestRoute</code>) when calculating reachable areas.</p> <p>Default value: <code>FastestRoute</code> </p>"""
    origin: NotRequired["aws_sdk_geo_routes.types.position.Position"]
    """<p>The starting point for isoline calculations, specified as <code>[longitude, latitude]</code> coordinates. For example, this could be a store location, service center, or any point from which you want to calculate reachable areas. Either <code>Origin</code> or <code>Destination</code> must be provided.</p>"""
    origin_options: NotRequired[
        "aws_sdk_geo_routes.types.isoline_origin_options.IsolineOriginOptions"
    ]
    """<p>Options that control how the origin point is matched to the road network and how routes can depart from it. These options help improve travel time accuracy by accounting for real-world access from the origin.</p>"""
    thresholds: "aws_sdk_geo_routes.types.isoline_thresholds.IsolineThresholds"
    r"""<p>The distance or time thresholds used to determine reachable areas. You can specify up to five thresholds (which all must be the same type) to calculate multiple isolines in a single request. For example, to determine the areas that are reachable within 10 and 20 minutes of the origin, specify time thresholds of 600 and 1200 seconds.</p> <p>You incur a calculation charge for each threshold. Using a large number of thresholds in a request can lead to unexpected charges. For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html\">Routes pricing</a> in the <i>Amazon Location Service Developer Guide</i>.</p>"""
    traffic: NotRequired[
        "aws_sdk_geo_routes.types.isoline_traffic_options.IsolineTrafficOptions"
    ]
    """<p>Configures how real-time and historical traffic data affects isoline calculations. Traffic patterns can significantly impact reachable areas, especially during peak hours.</p>"""
    travel_mode: NotRequired[
        "aws_sdk_geo_routes.types.isoline_travel_mode.IsolineTravelMode"
    ]
    """<p>The mode of transportation to use for calculations. This affects which road types or features can be used, estimated speed, and the traffic levels that are applied.</p> <ul> <li> <p> <code>Car</code>—Standard passenger vehicle routing using roads accessible to cars</p> </li> <li> <p> <code>Pedestrian</code>—Walking routes using pedestrian paths, sidewalks, and crossings</p> </li> <li> <p> <code>Scooter</code>—Light two-wheeled vehicle routing using roads and paths accessible to scooters</p> </li> <li> <p> <code>Truck</code>—Commercial truck routing considering vehicle dimensions, weight restrictions, and hazardous material regulations</p> </li> </ul> <note> <p>The mode <code>Scooter</code> also applies to motorcycles; set this to <code>Scooter</code> when calculating isolines for motorcycles.</p> </note> <p>Default value: <code>Car</code> </p>"""
    travel_mode_options: NotRequired[
        "aws_sdk_geo_routes.types.isoline_travel_mode_options.IsolineTravelModeOptions"
    ]
    """<p>Additional attributes that refine how reachable areas are calculated based on specific vehicle characteristics. These options help produce more accurate results by accounting for real-world constraints and capabilities.</p> <p>For example:</p> <ul> <li> <p>For trucks (<code>Truck</code>), specify dimensions, weight limits, and hazardous cargo restrictions to ensure isolines only include roads that can physically and legally accommodate the vehicle</p> </li> <li> <p>For cars (<code>Car</code>), set maximum speed capabilities or indicate high-occupancy vehicle eligibility to better estimate reachable areas</p> </li> <li> <p>For scooters (<code>Scooter</code>), specify engine type and speed limitations to more accurately model their travel capabilities</p> </li> </ul> <p>Without these options, calculations use default assumptions that may not match your specific use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateIsolinesRequest) -> dict:
    out: dict = {}
    if "allow" in value:
        import aws_sdk_geo_routes.types.isoline_allow_options

        out["Allow"] = aws_sdk_geo_routes.types.isoline_allow_options.serialize_json(
            value["allow"]
        )
    if "arrival_time" in value:
        out["ArrivalTime"] = value["arrival_time"]
    if "avoid" in value:
        import aws_sdk_geo_routes.types.isoline_avoidance_options

        out["Avoid"] = (
            aws_sdk_geo_routes.types.isoline_avoidance_options.serialize_json(
                value["avoid"]
            )
        )
    if "depart_now" in value:
        out["DepartNow"] = value["depart_now"]
    if "departure_time" in value:
        out["DepartureTime"] = value["departure_time"]
    if "destination" in value:
        import aws_sdk_geo_routes.types.position

        out["Destination"] = aws_sdk_geo_routes.types.position.serialize_json(
            value["destination"]
        )
    if "destination_options" in value:
        import aws_sdk_geo_routes.types.isoline_destination_options

        out["DestinationOptions"] = (
            aws_sdk_geo_routes.types.isoline_destination_options.serialize_json(
                value["destination_options"]
            )
        )
    if "isoline_geometry_format" in value:
        import aws_sdk_geo_routes.types.geometry_format

        out["IsolineGeometryFormat"] = (
            aws_sdk_geo_routes.types.geometry_format.serialize_json(
                value["isoline_geometry_format"]
            )
        )
    if "isoline_granularity" in value:
        import aws_sdk_geo_routes.types.isoline_granularity_options

        out["IsolineGranularity"] = (
            aws_sdk_geo_routes.types.isoline_granularity_options.serialize_json(
                value["isoline_granularity"]
            )
        )
    if "optimize_isoline_for" in value:
        import aws_sdk_geo_routes.types.isoline_optimization_objective

        out["OptimizeIsolineFor"] = (
            aws_sdk_geo_routes.types.isoline_optimization_objective.serialize_json(
                value["optimize_isoline_for"]
            )
        )
    if "optimize_routing_for" in value:
        import aws_sdk_geo_routes.types.routing_objective

        out["OptimizeRoutingFor"] = (
            aws_sdk_geo_routes.types.routing_objective.serialize_json(
                value["optimize_routing_for"]
            )
        )
    if "origin" in value:
        import aws_sdk_geo_routes.types.position

        out["Origin"] = aws_sdk_geo_routes.types.position.serialize_json(
            value["origin"]
        )
    if "origin_options" in value:
        import aws_sdk_geo_routes.types.isoline_origin_options

        out["OriginOptions"] = (
            aws_sdk_geo_routes.types.isoline_origin_options.serialize_json(
                value["origin_options"]
            )
        )
    import aws_sdk_geo_routes.types.isoline_thresholds

    out["Thresholds"] = aws_sdk_geo_routes.types.isoline_thresholds.serialize_json(
        value["thresholds"]
    )
    if "traffic" in value:
        import aws_sdk_geo_routes.types.isoline_traffic_options

        out["Traffic"] = (
            aws_sdk_geo_routes.types.isoline_traffic_options.serialize_json(
                value["traffic"]
            )
        )
    if "travel_mode" in value:
        import aws_sdk_geo_routes.types.isoline_travel_mode

        out["TravelMode"] = aws_sdk_geo_routes.types.isoline_travel_mode.serialize_json(
            value["travel_mode"]
        )
    if "travel_mode_options" in value:
        import aws_sdk_geo_routes.types.isoline_travel_mode_options

        out["TravelModeOptions"] = (
            aws_sdk_geo_routes.types.isoline_travel_mode_options.serialize_json(
                value["travel_mode_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CalculateIsolinesRequest:
    out: CalculateIsolinesRequest = {}  # type: ignore[typeddict-item]
    if "Allow" in data:
        import aws_sdk_geo_routes.types.isoline_allow_options

        out["allow"] = aws_sdk_geo_routes.types.isoline_allow_options.deserialize_json(
            data["Allow"]
        )
    if "ArrivalTime" in data:
        out["arrival_time"] = data["ArrivalTime"]
    if "Avoid" in data:
        import aws_sdk_geo_routes.types.isoline_avoidance_options

        out["avoid"] = (
            aws_sdk_geo_routes.types.isoline_avoidance_options.deserialize_json(
                data["Avoid"]
            )
        )
    if "DepartNow" in data:
        out["depart_now"] = data["DepartNow"]
    if "DepartureTime" in data:
        out["departure_time"] = data["DepartureTime"]
    if "Destination" in data:
        import aws_sdk_geo_routes.types.position

        out["destination"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Destination"]
        )
    if "DestinationOptions" in data:
        import aws_sdk_geo_routes.types.isoline_destination_options

        out["destination_options"] = (
            aws_sdk_geo_routes.types.isoline_destination_options.deserialize_json(
                data["DestinationOptions"]
            )
        )
    if "IsolineGeometryFormat" in data:
        import aws_sdk_geo_routes.types.geometry_format

        out["isoline_geometry_format"] = (
            aws_sdk_geo_routes.types.geometry_format.deserialize_json(
                data["IsolineGeometryFormat"]
            )
        )
    if "IsolineGranularity" in data:
        import aws_sdk_geo_routes.types.isoline_granularity_options

        out["isoline_granularity"] = (
            aws_sdk_geo_routes.types.isoline_granularity_options.deserialize_json(
                data["IsolineGranularity"]
            )
        )
    if "OptimizeIsolineFor" in data:
        import aws_sdk_geo_routes.types.isoline_optimization_objective

        out["optimize_isoline_for"] = (
            aws_sdk_geo_routes.types.isoline_optimization_objective.deserialize_json(
                data["OptimizeIsolineFor"]
            )
        )
    if "OptimizeRoutingFor" in data:
        import aws_sdk_geo_routes.types.routing_objective

        out["optimize_routing_for"] = (
            aws_sdk_geo_routes.types.routing_objective.deserialize_json(
                data["OptimizeRoutingFor"]
            )
        )
    if "Origin" in data:
        import aws_sdk_geo_routes.types.position

        out["origin"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Origin"]
        )
    if "OriginOptions" in data:
        import aws_sdk_geo_routes.types.isoline_origin_options

        out["origin_options"] = (
            aws_sdk_geo_routes.types.isoline_origin_options.deserialize_json(
                data["OriginOptions"]
            )
        )
    if "Thresholds" in data:
        import aws_sdk_geo_routes.types.isoline_thresholds

        out["thresholds"] = (
            aws_sdk_geo_routes.types.isoline_thresholds.deserialize_json(
                data["Thresholds"]
            )
        )
    else:
        raise DeserializationError("CalculateIsolinesRequest.thresholds required")
    if "Traffic" in data:
        import aws_sdk_geo_routes.types.isoline_traffic_options

        out["traffic"] = (
            aws_sdk_geo_routes.types.isoline_traffic_options.deserialize_json(
                data["Traffic"]
            )
        )
    if "TravelMode" in data:
        import aws_sdk_geo_routes.types.isoline_travel_mode

        out["travel_mode"] = (
            aws_sdk_geo_routes.types.isoline_travel_mode.deserialize_json(
                data["TravelMode"]
            )
        )
    if "TravelModeOptions" in data:
        import aws_sdk_geo_routes.types.isoline_travel_mode_options

        out["travel_mode_options"] = (
            aws_sdk_geo_routes.types.isoline_travel_mode_options.deserialize_json(
                data["TravelModeOptions"]
            )
        )
    return out
