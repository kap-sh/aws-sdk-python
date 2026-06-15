"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTravelModeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_car_options
    import aws_sdk_geo_routes.types.route_intermodal_options
    import aws_sdk_geo_routes.types.route_pedestrian_options
    import aws_sdk_geo_routes.types.route_scooter_options
    import aws_sdk_geo_routes.types.route_transit_options
    import aws_sdk_geo_routes.types.route_truck_options


class RouteTravelModeOptions(TypedDict):
    car: NotRequired["aws_sdk_geo_routes.types.route_car_options.RouteCarOptions"]
    """<p>Travel mode options when the provided travel mode is <code>Car</code>.</p>"""
    pedestrian: NotRequired[
        "aws_sdk_geo_routes.types.route_pedestrian_options.RoutePedestrianOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Pedestrian</code>.</p>"""
    scooter: NotRequired[
        "aws_sdk_geo_routes.types.route_scooter_options.RouteScooterOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Scooter</code>. </p> <note> <p>When travel mode is set to <code>Scooter</code>, then the avoidance option <code>ControlledAccessHighways</code> defaults to <code>true</code>.</p> </note>"""
    truck: NotRequired["aws_sdk_geo_routes.types.route_truck_options.RouteTruckOptions"]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""
    intermodal: NotRequired[
        "aws_sdk_geo_routes.types.route_intermodal_options.RouteIntermodalOptions"
    ]
    r"""<p>Travel mode options when the provided travel mode is <code>Intermodal</code>.</p> <note> <p>Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> </note>"""
    transit: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_options.RouteTransitOptions"
    ]
    r"""<p>Travel mode options when the provided travel mode is <code>Transit</code>.</p> <note> <p>Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTravelModeOptions) -> dict:
    out: dict = {}
    if "car" in value:
        import aws_sdk_geo_routes.types.route_car_options

        out["Car"] = aws_sdk_geo_routes.types.route_car_options.serialize_json(
            value["car"]
        )
    if "pedestrian" in value:
        import aws_sdk_geo_routes.types.route_pedestrian_options

        out["Pedestrian"] = (
            aws_sdk_geo_routes.types.route_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    if "scooter" in value:
        import aws_sdk_geo_routes.types.route_scooter_options

        out["Scooter"] = aws_sdk_geo_routes.types.route_scooter_options.serialize_json(
            value["scooter"]
        )
    if "truck" in value:
        import aws_sdk_geo_routes.types.route_truck_options

        out["Truck"] = aws_sdk_geo_routes.types.route_truck_options.serialize_json(
            value["truck"]
        )
    if "intermodal" in value:
        import aws_sdk_geo_routes.types.route_intermodal_options

        out["Intermodal"] = (
            aws_sdk_geo_routes.types.route_intermodal_options.serialize_json(
                value["intermodal"]
            )
        )
    if "transit" in value:
        import aws_sdk_geo_routes.types.route_transit_options

        out["Transit"] = aws_sdk_geo_routes.types.route_transit_options.serialize_json(
            value["transit"]
        )
    return out


def deserialize_json(data: dict) -> RouteTravelModeOptions:
    out: RouteTravelModeOptions = {}  # type: ignore[typeddict-item]
    if "Car" in data:
        import aws_sdk_geo_routes.types.route_car_options

        out["car"] = aws_sdk_geo_routes.types.route_car_options.deserialize_json(
            data["Car"]
        )
    if "Pedestrian" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_options

        out["pedestrian"] = (
            aws_sdk_geo_routes.types.route_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    if "Scooter" in data:
        import aws_sdk_geo_routes.types.route_scooter_options

        out["scooter"] = (
            aws_sdk_geo_routes.types.route_scooter_options.deserialize_json(
                data["Scooter"]
            )
        )
    if "Truck" in data:
        import aws_sdk_geo_routes.types.route_truck_options

        out["truck"] = aws_sdk_geo_routes.types.route_truck_options.deserialize_json(
            data["Truck"]
        )
    if "Intermodal" in data:
        import aws_sdk_geo_routes.types.route_intermodal_options

        out["intermodal"] = (
            aws_sdk_geo_routes.types.route_intermodal_options.deserialize_json(
                data["Intermodal"]
            )
        )
    if "Transit" in data:
        import aws_sdk_geo_routes.types.route_transit_options

        out["transit"] = (
            aws_sdk_geo_routes.types.route_transit_options.deserialize_json(
                data["Transit"]
            )
        )
    return out
