"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_accessibility_attribute_list
    import aws_sdk_geo_routes.types.route_intermodal_pedestrian_options
    import aws_sdk_geo_routes.types.route_intermodal_rental_options
    import aws_sdk_geo_routes.types.route_intermodal_taxi_options
    import aws_sdk_geo_routes.types.route_intermodal_transit_options
    import aws_sdk_geo_routes.types.route_intermodal_vehicle_options


class RouteIntermodalOptions(TypedDict):
    accessibility_attributes: NotRequired[
        "aws_sdk_geo_routes.types.route_accessibility_attribute_list.RouteAccessibilityAttributeList"
    ]
    """<p>Accessibility attributes to consider when calculating the route.</p>"""
    max_transfers: NotRequired["int"]
    """<p>Maximum number of transfers allowed when calculating the route.</p>"""
    pedestrian: NotRequired[
        "aws_sdk_geo_routes.types.route_intermodal_pedestrian_options.RouteIntermodalPedestrianOptions"
    ]
    """<p>Options for the pedestrian leg of the intermodal route.</p>"""
    rental: NotRequired[
        "aws_sdk_geo_routes.types.route_intermodal_rental_options.RouteIntermodalRentalOptions"
    ]
    """<p>Options for the rental leg of the intermodal route.</p>"""
    taxi: NotRequired[
        "aws_sdk_geo_routes.types.route_intermodal_taxi_options.RouteIntermodalTaxiOptions"
    ]
    """<p>Options for the taxi leg of the intermodal route.</p>"""
    transit: NotRequired[
        "aws_sdk_geo_routes.types.route_intermodal_transit_options.RouteIntermodalTransitOptions"
    ]
    """<p>Options for the transit leg of the intermodal route.</p>"""
    vehicle: NotRequired[
        "aws_sdk_geo_routes.types.route_intermodal_vehicle_options.RouteIntermodalVehicleOptions"
    ]
    """<p>Options for the vehicle leg of the intermodal route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalOptions) -> dict:
    out: dict = {}
    if "accessibility_attributes" in value:
        import aws_sdk_geo_routes.types.route_accessibility_attribute_list

        out["AccessibilityAttributes"] = (
            aws_sdk_geo_routes.types.route_accessibility_attribute_list.serialize_json(
                value["accessibility_attributes"]
            )
        )
    if "max_transfers" in value:
        out["MaxTransfers"] = value["max_transfers"]
    if "pedestrian" in value:
        import aws_sdk_geo_routes.types.route_intermodal_pedestrian_options

        out["Pedestrian"] = (
            aws_sdk_geo_routes.types.route_intermodal_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    if "rental" in value:
        import aws_sdk_geo_routes.types.route_intermodal_rental_options

        out["Rental"] = (
            aws_sdk_geo_routes.types.route_intermodal_rental_options.serialize_json(
                value["rental"]
            )
        )
    if "taxi" in value:
        import aws_sdk_geo_routes.types.route_intermodal_taxi_options

        out["Taxi"] = (
            aws_sdk_geo_routes.types.route_intermodal_taxi_options.serialize_json(
                value["taxi"]
            )
        )
    if "transit" in value:
        import aws_sdk_geo_routes.types.route_intermodal_transit_options

        out["Transit"] = (
            aws_sdk_geo_routes.types.route_intermodal_transit_options.serialize_json(
                value["transit"]
            )
        )
    if "vehicle" in value:
        import aws_sdk_geo_routes.types.route_intermodal_vehicle_options

        out["Vehicle"] = (
            aws_sdk_geo_routes.types.route_intermodal_vehicle_options.serialize_json(
                value["vehicle"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteIntermodalOptions:
    out: RouteIntermodalOptions = {}  # type: ignore[typeddict-item]
    if "AccessibilityAttributes" in data:
        import aws_sdk_geo_routes.types.route_accessibility_attribute_list

        out["accessibility_attributes"] = (
            aws_sdk_geo_routes.types.route_accessibility_attribute_list.deserialize_json(
                data["AccessibilityAttributes"]
            )
        )
    if "MaxTransfers" in data:
        out["max_transfers"] = data["MaxTransfers"]
    if "Pedestrian" in data:
        import aws_sdk_geo_routes.types.route_intermodal_pedestrian_options

        out["pedestrian"] = (
            aws_sdk_geo_routes.types.route_intermodal_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    if "Rental" in data:
        import aws_sdk_geo_routes.types.route_intermodal_rental_options

        out["rental"] = (
            aws_sdk_geo_routes.types.route_intermodal_rental_options.deserialize_json(
                data["Rental"]
            )
        )
    if "Taxi" in data:
        import aws_sdk_geo_routes.types.route_intermodal_taxi_options

        out["taxi"] = (
            aws_sdk_geo_routes.types.route_intermodal_taxi_options.deserialize_json(
                data["Taxi"]
            )
        )
    if "Transit" in data:
        import aws_sdk_geo_routes.types.route_intermodal_transit_options

        out["transit"] = (
            aws_sdk_geo_routes.types.route_intermodal_transit_options.deserialize_json(
                data["Transit"]
            )
        )
    if "Vehicle" in data:
        import aws_sdk_geo_routes.types.route_intermodal_vehicle_options

        out["vehicle"] = (
            aws_sdk_geo_routes.types.route_intermodal_vehicle_options.deserialize_json(
                data["Vehicle"]
            )
        )
    return out
