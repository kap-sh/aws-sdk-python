"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalTransitOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_intermodal_enabled_legs_list
    import aws_sdk_geo_routes.types.route_transit_mode_list


class RouteIntermodalTransitOptions(TypedDict, closed=True):
    allowed_modes: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Allowed transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>ExcludedModes</code>.</p>"""
    enabled_for: NotRequired[
        "aws_sdk_geo_routes.types.route_intermodal_enabled_legs_list.RouteIntermodalEnabledLegsList"
    ]
    """<p>Specifies the portion of the route for which this leg type is enabled. By default, the leg type is enabled for all legs. Valid values:</p> <ul> <li> <p> <code>FirstLeg</code> - Enable this leg type for the first non-pedestrian leg of the route.</p> </li> <li> <p> <code>LastLeg</code> - Enable this leg type for the last non-pedestrian leg of the route.</p> </li> <li> <p> <code>EntireRoute</code> - Enable this leg type for the entire route.</p> </li> <li> <p> <code>None</code> - Disable this leg type entirely.</p> </li> </ul>"""
    excluded_modes: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Excluded transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>AllowedModes</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalTransitOptions) -> dict:
    out: dict = {}
    if "allowed_modes" in value:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["AllowedModes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.serialize_json(
                value["allowed_modes"]
            )
        )
    if "enabled_for" in value:
        import aws_sdk_geo_routes.types.route_intermodal_enabled_legs_list

        out["EnabledFor"] = (
            aws_sdk_geo_routes.types.route_intermodal_enabled_legs_list.serialize_json(
                value["enabled_for"]
            )
        )
    if "excluded_modes" in value:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["ExcludedModes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.serialize_json(
                value["excluded_modes"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteIntermodalTransitOptions:
    out: RouteIntermodalTransitOptions = {}  # type: ignore[typeddict-item]
    if "AllowedModes" in data:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["allowed_modes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["AllowedModes"]
            )
        )
    if "EnabledFor" in data:
        import aws_sdk_geo_routes.types.route_intermodal_enabled_legs_list

        out["enabled_for"] = (
            aws_sdk_geo_routes.types.route_intermodal_enabled_legs_list.deserialize_json(
                data["EnabledFor"]
            )
        )
    if "ExcludedModes" in data:
        import aws_sdk_geo_routes.types.route_transit_mode_list

        out["excluded_modes"] = (
            aws_sdk_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["ExcludedModes"]
            )
        )
    return out
