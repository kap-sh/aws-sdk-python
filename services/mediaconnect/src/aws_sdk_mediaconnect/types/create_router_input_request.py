"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateRouterInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.maintenance_configuration
    import aws_sdk_mediaconnect.types.router_input_configuration
    import aws_sdk_mediaconnect.types.router_input_tier
    import aws_sdk_mediaconnect.types.router_input_transit_encryption
    import aws_sdk_mediaconnect.types.routing_scope


class CreateRouterInputRequest(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router input.</p>"""
    configuration: (
        "aws_sdk_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
    )
    """<p>The configuration settings for the router input, which can include the protocol, network interface, and other details.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate for the router input.</p>"""
    routing_scope: "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.</p>"""
    tier: "aws_sdk_mediaconnect.types.router_input_tier.RouterInputTier"
    """<p>The tier level for the router input.</p>"""
    region_name: NotRequired["str"]
    """<p>The Amazon Web Services Region for the router input. Defaults to the current region if not specified.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>"""
    transit_encryption: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
    ]
    """<p>The transit encryption settings for the router input.</p>"""
    maintenance_configuration: NotRequired[
        "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    ]
    """<p>The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.</p>"""
    tags: NotRequired["aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p>Key-value pairs that can be used to tag and organize this router input.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique identifier for the request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouterInputRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_input_configuration

    out["configuration"] = (
        aws_sdk_mediaconnect.types.router_input_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["maximumBitrate"] = value["maximum_bitrate"]
    import aws_sdk_mediaconnect.types.routing_scope

    out["routingScope"] = aws_sdk_mediaconnect.types.routing_scope.serialize_json(
        value["routing_scope"]
    )
    import aws_sdk_mediaconnect.types.router_input_tier

    out["tier"] = aws_sdk_mediaconnect.types.router_input_tier.serialize_json(
        value["tier"]
    )
    if "region_name" in value:
        out["regionName"] = value["region_name"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
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
    if "tags" in value:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRouterInputRequest:
    out: CreateRouterInputRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRouterInputRequest.name required")
    if "configuration" in data:
        import aws_sdk_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            aws_sdk_mediaconnect.types.router_input_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateRouterInputRequest.configuration required")
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        raise DeserializationError("CreateRouterInputRequest.maximum_bitrate required")
    if "routingScope" in data:
        import aws_sdk_mediaconnect.types.routing_scope

        out["routing_scope"] = (
            aws_sdk_mediaconnect.types.routing_scope.deserialize_json(
                data["routingScope"]
            )
        )
    else:
        raise DeserializationError("CreateRouterInputRequest.routing_scope required")
    if "tier" in data:
        import aws_sdk_mediaconnect.types.router_input_tier

        out["tier"] = aws_sdk_mediaconnect.types.router_input_tier.deserialize_json(
            data["tier"]
        )
    else:
        raise DeserializationError("CreateRouterInputRequest.tier required")
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
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
    if "tags" in data:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
