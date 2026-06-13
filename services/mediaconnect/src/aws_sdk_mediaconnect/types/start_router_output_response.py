"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StartRouterOutputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.maintenance_schedule
    import aws_sdk_mediaconnect.types.maintenance_schedule_type
    import aws_sdk_mediaconnect.types.router_output_arn
    import aws_sdk_mediaconnect.types.router_output_state


class StartRouterOutputResponse(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that was started.</p>"""
    name: "str"
    """<p>The name of the router output that was started.</p>"""
    state: "aws_sdk_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The current state of the router output after being started.</p>"""
    maintenance_schedule_type: (
        "aws_sdk_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    )
    """<p>The type of maintenance schedule associated with the router output.</p>"""
    maintenance_schedule: (
        "aws_sdk_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    )
    """<p>The details of the maintenance schedule for the router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRouterOutputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_output_state

    out["state"] = aws_sdk_mediaconnect.types.router_output_state.serialize_json(
        value["state"]
    )
    import aws_sdk_mediaconnect.types.maintenance_schedule_type

    out["maintenanceScheduleType"] = (
        aws_sdk_mediaconnect.types.maintenance_schedule_type.serialize_json(
            value["maintenance_schedule_type"]
        )
    )
    import aws_sdk_mediaconnect.types.maintenance_schedule

    out["maintenanceSchedule"] = (
        aws_sdk_mediaconnect.types.maintenance_schedule.serialize_json(
            value["maintenance_schedule"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartRouterOutputResponse:
    out: StartRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StartRouterOutputResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartRouterOutputResponse.name required")
    if "state" in data:
        import aws_sdk_mediaconnect.types.router_output_state

        out["state"] = aws_sdk_mediaconnect.types.router_output_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("StartRouterOutputResponse.state required")
    if "maintenanceScheduleType" in data:
        import aws_sdk_mediaconnect.types.maintenance_schedule_type

        out["maintenance_schedule_type"] = (
            aws_sdk_mediaconnect.types.maintenance_schedule_type.deserialize_json(
                data["maintenanceScheduleType"]
            )
        )
    else:
        raise DeserializationError(
            "StartRouterOutputResponse.maintenance_schedule_type required"
        )
    if "maintenanceSchedule" in data:
        import aws_sdk_mediaconnect.types.maintenance_schedule

        out["maintenance_schedule"] = (
            aws_sdk_mediaconnect.types.maintenance_schedule.deserialize_json(
                data["maintenanceSchedule"]
            )
        )
    else:
        raise DeserializationError(
            "StartRouterOutputResponse.maintenance_schedule required"
        )
    return out
