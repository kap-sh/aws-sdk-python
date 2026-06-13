"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateRouterOutputRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.maintenance_configuration
    import aws_sdk_mediaconnect.types.router_output_configuration
    import aws_sdk_mediaconnect.types.router_output_tier
    import aws_sdk_mediaconnect.types.routing_scope


class CreateRouterOutputRequest(TypedDict):
    name: "str"
    """<p>The name of the router output.</p>"""
    configuration: "aws_sdk_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
    """<p>The configuration settings for the router output.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate for the router output.</p>"""
    routing_scope: "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>"""
    tier: "aws_sdk_mediaconnect.types.router_output_tier.RouterOutputTier"
    """<p>The tier level for the router output.</p>"""
    region_name: NotRequired["str"]
    """<p>The Amazon Web Services Region for the router output. Defaults to the current region if not specified.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone where you want to create the router output. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>"""
    maintenance_configuration: NotRequired[
        "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    ]
    """<p>The maintenance configuration settings for the router output, including preferred maintenance windows and schedules.</p>"""
    tags: NotRequired["aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p>Key-value pairs that can be used to tag this router output.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique identifier for the request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouterOutputRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_output_configuration

    out["configuration"] = (
        aws_sdk_mediaconnect.types.router_output_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["maximumBitrate"] = value["maximum_bitrate"]
    import aws_sdk_mediaconnect.types.routing_scope

    out["routingScope"] = aws_sdk_mediaconnect.types.routing_scope.serialize_json(
        value["routing_scope"]
    )
    import aws_sdk_mediaconnect.types.router_output_tier

    out["tier"] = aws_sdk_mediaconnect.types.router_output_tier.serialize_json(
        value["tier"]
    )
    if "region_name" in value:
        out["regionName"] = value["region_name"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "maintenance_configuration" in value:
        import aws_sdk_mediaconnect.types.maintenance_configuration

        out["maintenanceConfiguration"] = (
            aws_sdk_mediaconnect.types.maintenance_configuration.serialize_json(
                value["maintenance_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRouterOutputRequest:
    out: CreateRouterOutputRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRouterOutputRequest.name required")
    if "configuration" in data:
        import aws_sdk_mediaconnect.types.router_output_configuration

        out["configuration"] = (
            aws_sdk_mediaconnect.types.router_output_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateRouterOutputRequest.configuration required")
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        raise DeserializationError("CreateRouterOutputRequest.maximum_bitrate required")
    if "routingScope" in data:
        import aws_sdk_mediaconnect.types.routing_scope

        out["routing_scope"] = (
            aws_sdk_mediaconnect.types.routing_scope.deserialize_json(
                data["routingScope"]
            )
        )
    else:
        raise DeserializationError("CreateRouterOutputRequest.routing_scope required")
    if "tier" in data:
        import aws_sdk_mediaconnect.types.router_output_tier

        out["tier"] = aws_sdk_mediaconnect.types.router_output_tier.deserialize_json(
            data["tier"]
        )
    else:
        raise DeserializationError("CreateRouterOutputRequest.tier required")
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "maintenanceConfiguration" in data:
        import aws_sdk_mediaconnect.types.maintenance_configuration

        out["maintenance_configuration"] = (
            aws_sdk_mediaconnect.types.maintenance_configuration.deserialize_json(
                data["maintenanceConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
