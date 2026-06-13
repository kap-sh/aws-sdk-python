"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediaconnect.types.maintenance_schedule
    import aws_sdk_mediaconnect.types.maintenance_schedule_type
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_network_interface_arn
    import aws_sdk_mediaconnect.types.router_output_arn
    import aws_sdk_mediaconnect.types.router_output_routed_state
    import aws_sdk_mediaconnect.types.router_output_state
    import aws_sdk_mediaconnect.types.router_output_type
    import aws_sdk_mediaconnect.types.routing_scope


class ListedRouterOutput(TypedDict):
    name: "str"
    """<p>The name of the router output.</p>"""
    arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output.</p>"""
    id: "str"
    """<p>The unique identifier of the router output.</p>"""
    output_type: "aws_sdk_mediaconnect.types.router_output_type.RouterOutputType"
    """<p>The type of the router output.</p>"""
    state: "aws_sdk_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The overall state of the router output.</p>"""
    routed_state: (
        "aws_sdk_mediaconnect.types.router_output_routed_state.RouterOutputRoutedState"
    )
    """<p>The current state of the association between the router output and its input.</p>"""
    region_name: "str"
    """<p>The AAmazon Web Services Region where the router output is located.</p>"""
    availability_zone: "str"
    """<p>The Availability Zone of the router output.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate of the router output.</p>"""
    routing_scope: "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Indicates whether the router output is configured for Regional or global routing.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router output was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router output was last updated.</p>"""
    message_count: "int"
    """<p>The number of messages associated with the router output.</p>"""
    routed_input_arn: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    ]
    """<p>The ARN of the router input associated with the output.</p>"""
    network_interface_arn: NotRequired[
        "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    ]
    """<p>The ARN of the network interface associated with the router output.</p>"""
    maintenance_schedule_type: NotRequired[
        "aws_sdk_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    ]
    """<p>The type of maintenance schedule currently associated with the listed router output.</p>"""
    maintenance_schedule: NotRequired[
        "aws_sdk_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The details of the maintenance schedule for the listed router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import aws_sdk_mediaconnect.types.router_output_type

    out["outputType"] = aws_sdk_mediaconnect.types.router_output_type.serialize_json(
        value["output_type"]
    )
    import aws_sdk_mediaconnect.types.router_output_state

    out["state"] = aws_sdk_mediaconnect.types.router_output_state.serialize_json(
        value["state"]
    )
    import aws_sdk_mediaconnect.types.router_output_routed_state

    out["routedState"] = (
        aws_sdk_mediaconnect.types.router_output_routed_state.serialize_json(
            value["routed_state"]
        )
    )
    out["regionName"] = value["region_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["maximumBitrate"] = value["maximum_bitrate"]
    import aws_sdk_mediaconnect.types.routing_scope

    out["routingScope"] = aws_sdk_mediaconnect.types.routing_scope.serialize_json(
        value["routing_scope"]
    )
    import aws_sdk_mediaconnect.types._prelude.timestamp

    out["createdAt"] = aws_sdk_mediaconnect.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_mediaconnect.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_mediaconnect.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    out["messageCount"] = value["message_count"]
    if "routed_input_arn" in value:
        out["routedInputArn"] = value["routed_input_arn"]
    if "network_interface_arn" in value:
        out["networkInterfaceArn"] = value["network_interface_arn"]
    if "maintenance_schedule_type" in value:
        import aws_sdk_mediaconnect.types.maintenance_schedule_type

        out["maintenanceScheduleType"] = (
            aws_sdk_mediaconnect.types.maintenance_schedule_type.serialize_json(
                value["maintenance_schedule_type"]
            )
        )
    if "maintenance_schedule" in value:
        import aws_sdk_mediaconnect.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            aws_sdk_mediaconnect.types.maintenance_schedule.serialize_json(
                value["maintenance_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListedRouterOutput:
    out: ListedRouterOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ListedRouterOutput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListedRouterOutput.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListedRouterOutput.id required")
    if "outputType" in data:
        import aws_sdk_mediaconnect.types.router_output_type

        out["output_type"] = (
            aws_sdk_mediaconnect.types.router_output_type.deserialize_json(
                data["outputType"]
            )
        )
    else:
        raise DeserializationError("ListedRouterOutput.output_type required")
    if "state" in data:
        import aws_sdk_mediaconnect.types.router_output_state

        out["state"] = aws_sdk_mediaconnect.types.router_output_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("ListedRouterOutput.state required")
    if "routedState" in data:
        import aws_sdk_mediaconnect.types.router_output_routed_state

        out["routed_state"] = (
            aws_sdk_mediaconnect.types.router_output_routed_state.deserialize_json(
                data["routedState"]
            )
        )
    else:
        raise DeserializationError("ListedRouterOutput.routed_state required")
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    else:
        raise DeserializationError("ListedRouterOutput.region_name required")
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError("ListedRouterOutput.availability_zone required")
    if "maximumBitrate" in data:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        raise DeserializationError("ListedRouterOutput.maximum_bitrate required")
    if "routingScope" in data:
        import aws_sdk_mediaconnect.types.routing_scope

        out["routing_scope"] = (
            aws_sdk_mediaconnect.types.routing_scope.deserialize_json(
                data["routingScope"]
            )
        )
    else:
        raise DeserializationError("ListedRouterOutput.routing_scope required")
    if "createdAt" in data:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ListedRouterOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("ListedRouterOutput.updated_at required")
    if "messageCount" in data:
        out["message_count"] = data["messageCount"]
    else:
        raise DeserializationError("ListedRouterOutput.message_count required")
    if "routedInputArn" in data:
        out["routed_input_arn"] = data["routedInputArn"]
    if "networkInterfaceArn" in data:
        out["network_interface_arn"] = data["networkInterfaceArn"]
    if "maintenanceScheduleType" in data:
        import aws_sdk_mediaconnect.types.maintenance_schedule_type

        out["maintenance_schedule_type"] = (
            aws_sdk_mediaconnect.types.maintenance_schedule_type.deserialize_json(
                data["maintenanceScheduleType"]
            )
        )
    if "maintenanceSchedule" in data:
        import aws_sdk_mediaconnect.types.maintenance_schedule

        out["maintenance_schedule"] = (
            aws_sdk_mediaconnect.types.maintenance_schedule.deserialize_json(
                data["maintenanceSchedule"]
            )
        )
    return out
