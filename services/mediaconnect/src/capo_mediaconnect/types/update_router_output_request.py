"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.router_output_arn
    import capo_mediaconnect.types.router_output_configuration
    import capo_mediaconnect.types.router_output_tier
    import capo_mediaconnect.types.routing_scope


class UpdateRouterOutputRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that you want to update.</p>"""
    name: NotRequired["str"]
    """<p>The updated name for the router output.</p>"""
    configuration: NotRequired[
        "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
    ]
    """<p>The updated configuration settings for the router output. Changing the type of the configuration is not supported.</p>"""
    maximum_bitrate: NotRequired["int"]
    """<p>The updated maximum bitrate for the router output.</p>"""
    routing_scope: NotRequired["capo_mediaconnect.types.routing_scope.RoutingScope"]
    """<p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>"""
    tier: NotRequired["capo_mediaconnect.types.router_output_tier.RouterOutputTier"]
    """<p>The updated tier level for the router output.</p>"""
    maintenance_configuration: NotRequired[
        "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    ]
    """<p>The updated maintenance configuration settings for the router output, including any changes to preferred maintenance windows and schedules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterOutputRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import capo_mediaconnect.types.router_output_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_output_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "maximum_bitrate" in value:
        out["maximumBitrate"] = value["maximum_bitrate"]
    if "routing_scope" in value:
        import capo_mediaconnect.types.routing_scope

        out["routingScope"] = capo_mediaconnect.types.routing_scope.serialize_json(
            value["routing_scope"]
        )
    if "tier" in value:
        import capo_mediaconnect.types.router_output_tier

        out["tier"] = capo_mediaconnect.types.router_output_tier.serialize_json(
            value["tier"]
        )
    if "maintenance_configuration" in value:
        import capo_mediaconnect.types.maintenance_configuration

        out["maintenanceConfiguration"] = (
            capo_mediaconnect.types.maintenance_configuration.serialize_json(
                value["maintenance_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRouterOutputRequest:
    out: UpdateRouterOutputRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "configuration" in data:
        import capo_mediaconnect.types.router_output_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_output_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    if "routingScope" in data:
        import capo_mediaconnect.types.routing_scope

        out["routing_scope"] = capo_mediaconnect.types.routing_scope.deserialize_json(
            data["routingScope"]
        )
    if "tier" in data:
        import capo_mediaconnect.types.router_output_tier

        out["tier"] = capo_mediaconnect.types.router_output_tier.deserialize_json(
            data["tier"]
        )
    if "maintenanceConfiguration" in data:
        import capo_mediaconnect.types.maintenance_configuration

        out["maintenance_configuration"] = (
            capo_mediaconnect.types.maintenance_configuration.deserialize_json(
                data["maintenanceConfiguration"]
            )
        )
    return out
