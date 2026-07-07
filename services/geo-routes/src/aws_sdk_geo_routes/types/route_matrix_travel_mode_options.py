"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTravelModeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_car_options
    import aws_sdk_geo_routes.types.route_matrix_scooter_options
    import aws_sdk_geo_routes.types.route_matrix_truck_options


class RouteMatrixTravelModeOptions(TypedDict, closed=True):
    car: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_car_options.RouteMatrixCarOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Car</code>.</p>"""
    scooter: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_scooter_options.RouteMatrixScooterOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Scooter</code>. </p> <note> <p>When travel mode is set to <code>Scooter</code>, then the avoidance option <code>ControlledAccessHighways</code> defaults to <code>true</code>.</p> </note>"""
    truck: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_truck_options.RouteMatrixTruckOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixTravelModeOptions) -> dict:
    out: dict = {}
    if "car" in value:
        import aws_sdk_geo_routes.types.route_matrix_car_options

        out["Car"] = aws_sdk_geo_routes.types.route_matrix_car_options.serialize_json(
            value["car"]
        )
    if "scooter" in value:
        import aws_sdk_geo_routes.types.route_matrix_scooter_options

        out["Scooter"] = (
            aws_sdk_geo_routes.types.route_matrix_scooter_options.serialize_json(
                value["scooter"]
            )
        )
    if "truck" in value:
        import aws_sdk_geo_routes.types.route_matrix_truck_options

        out["Truck"] = (
            aws_sdk_geo_routes.types.route_matrix_truck_options.serialize_json(
                value["truck"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixTravelModeOptions:
    out: RouteMatrixTravelModeOptions = {}  # type: ignore[typeddict-item]
    if "Car" in data:
        import aws_sdk_geo_routes.types.route_matrix_car_options

        out["car"] = aws_sdk_geo_routes.types.route_matrix_car_options.deserialize_json(
            data["Car"]
        )
    if "Scooter" in data:
        import aws_sdk_geo_routes.types.route_matrix_scooter_options

        out["scooter"] = (
            aws_sdk_geo_routes.types.route_matrix_scooter_options.deserialize_json(
                data["Scooter"]
            )
        )
    if "Truck" in data:
        import aws_sdk_geo_routes.types.route_matrix_truck_options

        out["truck"] = (
            aws_sdk_geo_routes.types.route_matrix_truck_options.deserialize_json(
                data["Truck"]
            )
        )
    return out
