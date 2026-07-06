"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_accessibility_attribute_list
    import aws_sdk_geo_routes.types.route_transit_mode_list
    import aws_sdk_geo_routes.types.route_transit_pedestrian_options


class RouteTransitOptions(TypedDict, closed=True):
    accessibility_attributes: NotRequired[
        "aws_sdk_geo_routes.types.route_accessibility_attribute_list.RouteAccessibilityAttributeList"
    ]
    """<p>Accessibility attributes to consider when calculating the route.</p>"""
    allowed_modes: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Allowed transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>ExcludedModes</code>.</p>"""
    excluded_modes: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Excluded transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>AllowedModes</code>.</p>"""
    max_transfers: NotRequired["int"]
    """<p>Maximum number of transfers allowed when calculating the route.</p>"""
    pedestrian: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_pedestrian_options.RouteTransitPedestrianOptions"
    ]
    """<p>Options for the pedestrian leg of the transit route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitOptions) -> dict:
    out: dict = {}
    if "accessibility_attributes" in value:
        import aws_sdk_geo_routes.types.route_accessibility_attribute_list

        out["AccessibilityAttributes"] = (
            aws_sdk_geo_routes.types.route_accessibility_attribute_list.serialize_json(
                value["accessibility_attributes"]
            )
        )
    if "allowed_modes" in value:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["AllowedModes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.serialize_json(
                value["allowed_modes"]
            )
        )
    if "excluded_modes" in value:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["ExcludedModes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.serialize_json(
                value["excluded_modes"]
            )
        )
    if "max_transfers" in value:
        out["MaxTransfers"] = value["max_transfers"]
    if "pedestrian" in value:
        import aws_sdk_geo_routes.types.route_transit_pedestrian_options

        out["Pedestrian"] = (
            aws_sdk_geo_routes.types.route_transit_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTransitOptions:
    out: RouteTransitOptions = {}  # type: ignore[typeddict-item]
    if "AccessibilityAttributes" in data:
        import aws_sdk_geo_routes.types.route_accessibility_attribute_list

        out["accessibility_attributes"] = (
            aws_sdk_geo_routes.types.route_accessibility_attribute_list.deserialize_json(
                data["AccessibilityAttributes"]
            )
        )
    if "AllowedModes" in data:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["allowed_modes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["AllowedModes"]
            )
        )
    if "ExcludedModes" in data:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["excluded_modes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["ExcludedModes"]
            )
        )
    if "MaxTransfers" in data:
        out["max_transfers"] = data["MaxTransfers"]
    if "Pedestrian" in data:
        import aws_sdk_geo_routes.types.route_transit_pedestrian_options

        out["pedestrian"] = (
            aws_sdk_geo_routes.types.route_transit_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    return out
