"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.maintenance_configuration
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_input_configuration
    import aws_sdk_mediaconnect.types.router_input_tier
    import aws_sdk_mediaconnect.types.router_input_transit_encryption
    import aws_sdk_mediaconnect.types.routing_scope


class UpdateRouterInputRequest(TypedDict, closed=True):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that you want to update.</p>"""
    name: NotRequired["str"]
    """<p>The updated name for the router input.</p>"""
    configuration: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
    ]
    """<p>The updated configuration settings for the router input. Changing the type of the configuration is not supported.</p>"""
    maximum_bitrate: NotRequired["int"]
    """<p>The updated maximum bitrate for the router input.</p>"""
    routing_scope: NotRequired["aws_sdk_mediaconnect.types.routing_scope.RoutingScope"]
    """<p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.</p>"""
    tier: NotRequired["aws_sdk_mediaconnect.types.router_input_tier.RouterInputTier"]
    """<p>The updated tier level for the router input.</p>"""
    transit_encryption: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
    ]
    """<p>The updated transit encryption settings for the router input.</p>"""
    maintenance_configuration: NotRequired[
        "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    ]
    """<p>The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouterInputRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import aws_sdk_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            aws_sdk_mediaconnect.types.router_input_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "maximum_bitrate" in value:
        out["maximumBitrate"] = value["maximum_bitrate"]
    if "routing_scope" in value:
        import aws_sdk_mediaconnect.types.routing_scope

        out["routingScope"] = aws_sdk_mediaconnect.types.routing_scope.serialize_json(
            value["routing_scope"]
        )
    if "tier" in value:
        import aws_sdk_mediaconnect.types.router_input_tier

        out["tier"] = aws_sdk_mediaconnect.types.router_input_tier.serialize_json(
            value["tier"]
        )
    if "transit_encryption" in value:
        import aws_sdk_mediaconnect.types.router_input_transit_encryption

        out["transitEncryption"] = (
            aws_sdk_mediaconnect.types.router_input_transit_encryption.serialize_json(
                value["transit_encryption"]
            )
        )
    if "maintenance_configuration" in value:
        import aws_sdk_mediaconnect.types.maintenance_configuration

        out["maintenanceConfiguration"] = (
            aws_sdk_mediaconnect.types.maintenance_configuration.serialize_json(
                value["maintenance_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRouterInputRequest:
    out: UpdateRouterInputRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "configuration" in data:
        import aws_sdk_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            aws_sdk_mediaconnect.types.router_input_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    if "routingScope" in data:
        import aws_sdk_mediaconnect.types.routing_scope

        out["routing_scope"] = (
            aws_sdk_mediaconnect.types.routing_scope.deserialize_json(
                data["routingScope"]
            )
        )
    if "tier" in data:
        import aws_sdk_mediaconnect.types.router_input_tier

        out["tier"] = aws_sdk_mediaconnect.types.router_input_tier.deserialize_json(
            data["tier"]
        )
    if "transitEncryption" in data:
        import aws_sdk_mediaconnect.types.router_input_transit_encryption

        out["transit_encryption"] = (
            aws_sdk_mediaconnect.types.router_input_transit_encryption.deserialize_json(
                data["transitEncryption"]
            )
        )
    if "maintenanceConfiguration" in data:
        import aws_sdk_mediaconnect.types.maintenance_configuration

        out["maintenance_configuration"] = (
            aws_sdk_mediaconnect.types.maintenance_configuration.deserialize_json(
                data["maintenanceConfiguration"]
            )
        )
    return out
