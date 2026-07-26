"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.maintenance_schedule
    import capo_mediaconnect.types.maintenance_schedule_type
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_state
    import capo_mediaconnect.types.router_input_type
    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.routing_scope


class ListedRouterInput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router input.</p>"""
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input.</p>"""
    id: "str"
    """<p>The unique identifier of the router input.</p>"""
    input_type: "capo_mediaconnect.types.router_input_type.RouterInputType"
    """<p>The type of the router input.</p>"""
    state: "capo_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The overall state of the router input.</p>"""
    routed_outputs: "int"
    """<p>The number of router outputs that are associated with this router input.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router input is located.</p>"""
    availability_zone: "str"
    """<p>The Availability Zone of the router input.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate of the router input.</p>"""
    routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Indicates whether the router input is configured for Regional or global routing.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router input was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router input was last updated.</p>"""
    message_count: "int"
    """<p>The number of messages associated with the router input.</p>"""
    network_interface_arn: NotRequired[
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    ]
    """<p>The ARN of the network interface associated with the router input.</p>"""
    maintenance_schedule_type: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    ]
    """<p>The type of maintenance schedule currently associated with the listed router input.</p>"""
    maintenance_schedule: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The details of the maintenance schedule for the listed router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.router_input_type

    out["inputType"] = capo_mediaconnect.types.router_input_type.serialize_json(
        value["input_type"]
    )
    import capo_mediaconnect.types.router_input_state

    out["state"] = capo_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
    out["routedOutputs"] = value["routed_outputs"]
    out["regionName"] = value["region_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["maximumBitrate"] = value["maximum_bitrate"]
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
    out["messageCount"] = value["message_count"]
    if "network_interface_arn" in value:
        out["networkInterfaceArn"] = value["network_interface_arn"]
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


def deserialize_json(data: dict) -> ListedRouterInput:
    out: ListedRouterInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ListedRouterInput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListedRouterInput.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListedRouterInput.id required")
    if "inputType" in data:
        import capo_mediaconnect.types.router_input_type

        out["input_type"] = capo_mediaconnect.types.router_input_type.deserialize_json(
            data["inputType"]
        )
    else:
        raise DeserializationError("ListedRouterInput.input_type required")
    if "state" in data:
        import capo_mediaconnect.types.router_input_state

        out["state"] = capo_mediaconnect.types.router_input_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("ListedRouterInput.state required")
    if "routedOutputs" in data:
        out["routed_outputs"] = data["routedOutputs"]
    else:
        raise DeserializationError("ListedRouterInput.routed_outputs required")
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    else:
        raise DeserializationError("ListedRouterInput.region_name required")
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError("ListedRouterInput.availability_zone required")
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        raise DeserializationError("ListedRouterInput.maximum_bitrate required")
    if "routingScope" in data:
        import capo_mediaconnect.types.routing_scope

        out["routing_scope"] = capo_mediaconnect.types.routing_scope.deserialize_json(
            data["routingScope"]
        )
    else:
        raise DeserializationError("ListedRouterInput.routing_scope required")
    if "createdAt" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["created_at"] = capo_mediaconnect.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ListedRouterInput.created_at required")
    if "updatedAt" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["updated_at"] = capo_mediaconnect.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ListedRouterInput.updated_at required")
    if "messageCount" in data:
        out["message_count"] = data["messageCount"]
    else:
        raise DeserializationError("ListedRouterInput.message_count required")
    if "networkInterfaceArn" in data:
        out["network_interface_arn"] = data["networkInterfaceArn"]
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
