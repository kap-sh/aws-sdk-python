"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.maintenance_schedule
    import capo_mediaconnect.types.maintenance_schedule_type
    import capo_mediaconnect.types.maintenance_type
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_configuration
    import capo_mediaconnect.types.router_input_messages
    import capo_mediaconnect.types.router_input_state
    import capo_mediaconnect.types.router_input_stream_details
    import capo_mediaconnect.types.router_input_tier
    import capo_mediaconnect.types.router_input_transit_encryption
    import capo_mediaconnect.types.router_input_type
    import capo_mediaconnect.types.routing_scope


class RouterInput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router input.</p>"""
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input.</p>"""
    id: "str"
    """<p>The unique identifier of the router input.</p>"""
    state: "capo_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The current state of the router input.</p>"""
    input_type: "capo_mediaconnect.types.router_input_type.RouterInputType"
    """<p>The type of the router input.</p>"""
    configuration: (
        "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
    )
    routed_outputs: "int"
    """<p>The number of router outputs associated with the router input.</p>"""
    maximum_routed_outputs: NotRequired["int"]
    """<p>The maximum number of outputs that can be simultaneously routed to this input.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router input is located.</p>"""
    availability_zone: "str"
    """<p>The Availability Zone of the router input.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate for the router input.</p>"""
    tier: "capo_mediaconnect.types.router_input_tier.RouterInputTier"
    """<p>The tier level of the router input.</p>"""
    routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Indicates whether the router input is configured for Regional or global routing.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router input was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router input was last updated.</p>"""
    messages: "capo_mediaconnect.types.router_input_messages.RouterInputMessages"
    """<p>The messages associated with the router input.</p>"""
    transit_encryption: "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
    tags: "capo_mediaconnect.types.__map_of_string.__mapOfString"
    """<p>Key-value pairs that can be used to tag and organize this router input.</p>"""
    stream_details: (
        "capo_mediaconnect.types.router_input_stream_details.RouterInputStreamDetails"
    )
    ip_address: NotRequired["str"]
    """<p>The IP address of the router input.</p>"""
    maintenance_type: "capo_mediaconnect.types.maintenance_type.MaintenanceType"
    """<p>The type of maintenance configuration applied to this router input.</p>"""
    maintenance_configuration: (
        "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    )
    """<p>The maintenance configuration settings applied to this router input.</p>"""
    maintenance_schedule_type: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    ]
    """<p>The type of maintenance schedule currently in effect for this router input.</p>"""
    maintenance_schedule: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The current maintenance schedule details for this router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.router_input_state

    out["state"] = capo_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
    import capo_mediaconnect.types.router_input_type

    out["inputType"] = capo_mediaconnect.types.router_input_type.serialize_json(
        value["input_type"]
    )
    import capo_mediaconnect.types.router_input_configuration

    out["configuration"] = (
        capo_mediaconnect.types.router_input_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["routedOutputs"] = value["routed_outputs"]
    if "maximum_routed_outputs" in value:
        out["maximumRoutedOutputs"] = value["maximum_routed_outputs"]
    out["regionName"] = value["region_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["maximumBitrate"] = value["maximum_bitrate"]
    import capo_mediaconnect.types.router_input_tier

    out["tier"] = capo_mediaconnect.types.router_input_tier.serialize_json(
        value["tier"]
    )
    import capo_mediaconnect.types.routing_scope

    out["routingScope"] = capo_mediaconnect.types.routing_scope.serialize_json(
        value["routing_scope"]
    )
    import capo_mediaconnect.types._prelude.timestamp

    out["createdAt"] = capo_mediaconnect.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_mediaconnect.types._prelude.timestamp

    out["updatedAt"] = capo_mediaconnect.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    import capo_mediaconnect.types.router_input_messages

    out["messages"] = capo_mediaconnect.types.router_input_messages.serialize_json(
        value["messages"]
    )
    import capo_mediaconnect.types.router_input_transit_encryption

    out["transitEncryption"] = (
        capo_mediaconnect.types.router_input_transit_encryption.serialize_json(
            value["transit_encryption"]
        )
    )
    import capo_mediaconnect.types.__map_of_string

    out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(value["tags"])
    import capo_mediaconnect.types.router_input_stream_details

    out["streamDetails"] = (
        capo_mediaconnect.types.router_input_stream_details.serialize_json(
            value["stream_details"]
        )
    )
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    import capo_mediaconnect.types.maintenance_type

    out["maintenanceType"] = capo_mediaconnect.types.maintenance_type.serialize_json(
        value["maintenance_type"]
    )
    import capo_mediaconnect.types.maintenance_configuration

    out["maintenanceConfiguration"] = (
        capo_mediaconnect.types.maintenance_configuration.serialize_json(
            value["maintenance_configuration"]
        )
    )
    if "maintenance_schedule_type" in value:
        import capo_mediaconnect.types.maintenance_schedule_type

        out["maintenanceScheduleType"] = (
            capo_mediaconnect.types.maintenance_schedule_type.serialize_json(
                value["maintenance_schedule_type"]
            )
        )
    if "maintenance_schedule" in value:
        import capo_mediaconnect.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            capo_mediaconnect.types.maintenance_schedule.serialize_json(
                value["maintenance_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouterInput:
    out: RouterInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RouterInput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RouterInput.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RouterInput.id required")
    if "state" in data:
        import capo_mediaconnect.types.router_input_state

        out["state"] = capo_mediaconnect.types.router_input_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("RouterInput.state required")
    if "inputType" in data:
        import capo_mediaconnect.types.router_input_type

        out["input_type"] = capo_mediaconnect.types.router_input_type.deserialize_json(
            data["inputType"]
        )
    else:
        raise DeserializationError("RouterInput.input_type required")
    if "configuration" in data:
        import capo_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_input_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("RouterInput.configuration required")
    if "routedOutputs" in data:
        out["routed_outputs"] = data["routedOutputs"]
    else:
        raise DeserializationError("RouterInput.routed_outputs required")
    if "maximumRoutedOutputs" in data:
        out["maximum_routed_outputs"] = data["maximumRoutedOutputs"]
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    else:
        raise DeserializationError("RouterInput.region_name required")
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError("RouterInput.availability_zone required")
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        raise DeserializationError("RouterInput.maximum_bitrate required")
    if "tier" in data:
        import capo_mediaconnect.types.router_input_tier

        out["tier"] = capo_mediaconnect.types.router_input_tier.deserialize_json(
            data["tier"]
        )
    else:
        raise DeserializationError("RouterInput.tier required")
    if "routingScope" in data:
        import capo_mediaconnect.types.routing_scope

        out["routing_scope"] = capo_mediaconnect.types.routing_scope.deserialize_json(
            data["routingScope"]
        )
    else:
        raise DeserializationError("RouterInput.routing_scope required")
    if "createdAt" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["created_at"] = capo_mediaconnect.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("RouterInput.created_at required")
    if "updatedAt" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["updated_at"] = capo_mediaconnect.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("RouterInput.updated_at required")
    if "messages" in data:
        import capo_mediaconnect.types.router_input_messages

        out["messages"] = (
            capo_mediaconnect.types.router_input_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("RouterInput.messages required")
    if "transitEncryption" in data:
        import capo_mediaconnect.types.router_input_transit_encryption

        out["transit_encryption"] = (
            capo_mediaconnect.types.router_input_transit_encryption.deserialize_json(
                data["transitEncryption"]
            )
        )
    else:
        raise DeserializationError("RouterInput.transit_encryption required")
    if "tags" in data:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("RouterInput.tags required")
    if "streamDetails" in data:
        import capo_mediaconnect.types.router_input_stream_details

        out["stream_details"] = (
            capo_mediaconnect.types.router_input_stream_details.deserialize_json(
                data["streamDetails"]
            )
        )
    else:
        raise DeserializationError("RouterInput.stream_details required")
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "maintenanceType" in data:
        import capo_mediaconnect.types.maintenance_type

        out["maintenance_type"] = (
            capo_mediaconnect.types.maintenance_type.deserialize_json(
                data["maintenanceType"]
            )
        )
    else:
        raise DeserializationError("RouterInput.maintenance_type required")
    if "maintenanceConfiguration" in data:
        import capo_mediaconnect.types.maintenance_configuration

        out["maintenance_configuration"] = (
            capo_mediaconnect.types.maintenance_configuration.deserialize_json(
                data["maintenanceConfiguration"]
            )
        )
    else:
        raise DeserializationError("RouterInput.maintenance_configuration required")
    if "maintenanceScheduleType" in data:
        import capo_mediaconnect.types.maintenance_schedule_type

        out["maintenance_schedule_type"] = (
            capo_mediaconnect.types.maintenance_schedule_type.deserialize_json(
                data["maintenanceScheduleType"]
            )
        )
    if "maintenanceSchedule" in data:
        import capo_mediaconnect.types.maintenance_schedule

        out["maintenance_schedule"] = (
            capo_mediaconnect.types.maintenance_schedule.deserialize_json(
                data["maintenanceSchedule"]
            )
        )
    return out
