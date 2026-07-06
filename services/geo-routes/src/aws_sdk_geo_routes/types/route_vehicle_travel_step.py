"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleTravelStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.localized_string_list
    import aws_sdk_geo_routes.types.route_continue_highway_step_details
    import aws_sdk_geo_routes.types.route_continue_step_details
    import aws_sdk_geo_routes.types.route_enter_highway_step_details
    import aws_sdk_geo_routes.types.route_exit_step_details
    import aws_sdk_geo_routes.types.route_keep_step_details
    import aws_sdk_geo_routes.types.route_ramp_step_details
    import aws_sdk_geo_routes.types.route_road
    import aws_sdk_geo_routes.types.route_roundabout_enter_step_details
    import aws_sdk_geo_routes.types.route_roundabout_exit_step_details
    import aws_sdk_geo_routes.types.route_roundabout_pass_step_details
    import aws_sdk_geo_routes.types.route_signpost
    import aws_sdk_geo_routes.types.route_turn_step_details
    import aws_sdk_geo_routes.types.route_u_turn_step_details
    import aws_sdk_geo_routes.types.route_vehicle_travel_step_type
    import aws_sdk_geo_routes.types.sensitive_string


class RouteVehicleTravelStep(TypedDict, closed=True):
    continue_highway_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_continue_highway_step_details.RouteContinueHighwayStepDetails"
    ]
    """<p>Details that are specific to a Continue Highway step.</p>"""
    continue_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_continue_step_details.RouteContinueStepDetails"
    ]
    """<p>Details that are specific to a Continue step.</p>"""
    current_road: NotRequired["aws_sdk_geo_routes.types.route_road.RouteRoad"]
    """<p>Details of the current road.</p>"""
    distance: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the step.</p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    enter_highway_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_enter_highway_step_details.RouteEnterHighwayStepDetails"
    ]
    """<p>Details that are specific to a Enter Highway step.</p>"""
    exit_number: NotRequired[
        "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    ]
    """<p>Exit number of the road exit, if applicable.</p>"""
    exit_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_exit_step_details.RouteExitStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Exit step.</p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    instruction: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Brief description of the step in the requested language.</p> <note> <p>Only available when the TravelStepType is Default.</p> </note>"""
    keep_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_keep_step_details.RouteKeepStepDetails"
    ]
    """<p>Details that are specific to a Keep step.</p>"""
    next_road: NotRequired["aws_sdk_geo_routes.types.route_road.RouteRoad"]
    """<p>Details of the next road. See RouteRoad for details of sub-attributes.</p>"""
    ramp_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_ramp_step_details.RouteRampStepDetails"
    ]
    """<p>Details that are specific to a Ramp step.</p>"""
    roundabout_enter_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_roundabout_enter_step_details.RouteRoundaboutEnterStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Enter step.</p>"""
    roundabout_exit_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_roundabout_exit_step_details.RouteRoundaboutExitStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Exit step.</p>"""
    roundabout_pass_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_roundabout_pass_step_details.RouteRoundaboutPassStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Pass step.</p>"""
    signpost: NotRequired["aws_sdk_geo_routes.types.route_signpost.RouteSignpost"]
    """<p>Sign post information of the action, applicable only for TurnByTurn steps. See RouteSignpost for details of sub-attributes.</p>"""
    turn_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_turn_step_details.RouteTurnStepDetails"
    ]
    """<p>Details that are specific to a Turn step.</p>"""
    type: "aws_sdk_geo_routes.types.route_vehicle_travel_step_type.RouteVehicleTravelStepType"
    """<p>Type of the step.</p>"""
    u_turn_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_u_turn_step_details.RouteUTurnStepDetails"
    ]
    """<p>Details that are specific to a Turn step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleTravelStep) -> dict:
    out: dict = {}
    if "continue_highway_step_details" in value:
        import aws_sdk_geo_routes.types.route_continue_highway_step_details

        out["ContinueHighwayStepDetails"] = (
            aws_sdk_geo_routes.types.route_continue_highway_step_details.serialize_json(
                value["continue_highway_step_details"]
            )
        )
    if "continue_step_details" in value:
        import aws_sdk_geo_routes.types.route_continue_step_details

        out["ContinueStepDetails"] = (
            aws_sdk_geo_routes.types.route_continue_step_details.serialize_json(
                value["continue_step_details"]
            )
        )
    if "current_road" in value:
        import aws_sdk_geo_routes.types.route_road

        out["CurrentRoad"] = aws_sdk_geo_routes.types.route_road.serialize_json(
            value["current_road"]
        )
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "enter_highway_step_details" in value:
        import aws_sdk_geo_routes.types.route_enter_highway_step_details

        out["EnterHighwayStepDetails"] = (
            aws_sdk_geo_routes.types.route_enter_highway_step_details.serialize_json(
                value["enter_highway_step_details"]
            )
        )
    if "exit_number" in value:
        import aws_sdk_geo_routes.types.localized_string_list

        out["ExitNumber"] = (
            aws_sdk_geo_routes.types.localized_string_list.serialize_json(
                value["exit_number"]
            )
        )
    if "exit_step_details" in value:
        import aws_sdk_geo_routes.types.route_exit_step_details

        out["ExitStepDetails"] = (
            aws_sdk_geo_routes.types.route_exit_step_details.serialize_json(
                value["exit_step_details"]
            )
        )
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    if "keep_step_details" in value:
        import aws_sdk_geo_routes.types.route_keep_step_details

        out["KeepStepDetails"] = (
            aws_sdk_geo_routes.types.route_keep_step_details.serialize_json(
                value["keep_step_details"]
            )
        )
    if "next_road" in value:
        import aws_sdk_geo_routes.types.route_road

        out["NextRoad"] = aws_sdk_geo_routes.types.route_road.serialize_json(
            value["next_road"]
        )
    if "ramp_step_details" in value:
        import aws_sdk_geo_routes.types.route_ramp_step_details

        out["RampStepDetails"] = (
            aws_sdk_geo_routes.types.route_ramp_step_details.serialize_json(
                value["ramp_step_details"]
            )
        )
    if "roundabout_enter_step_details" in value:
        import aws_sdk_geo_routes.types.route_roundabout_enter_step_details

        out["RoundaboutEnterStepDetails"] = (
            aws_sdk_geo_routes.types.route_roundabout_enter_step_details.serialize_json(
                value["roundabout_enter_step_details"]
            )
        )
    if "roundabout_exit_step_details" in value:
        import aws_sdk_geo_routes.types.route_roundabout_exit_step_details

        out["RoundaboutExitStepDetails"] = (
            aws_sdk_geo_routes.types.route_roundabout_exit_step_details.serialize_json(
                value["roundabout_exit_step_details"]
            )
        )
    if "roundabout_pass_step_details" in value:
        import aws_sdk_geo_routes.types.route_roundabout_pass_step_details

        out["RoundaboutPassStepDetails"] = (
            aws_sdk_geo_routes.types.route_roundabout_pass_step_details.serialize_json(
                value["roundabout_pass_step_details"]
            )
        )
    if "signpost" in value:
        import aws_sdk_geo_routes.types.route_signpost

        out["Signpost"] = aws_sdk_geo_routes.types.route_signpost.serialize_json(
            value["signpost"]
        )
    if "turn_step_details" in value:
        import aws_sdk_geo_routes.types.route_turn_step_details

        out["TurnStepDetails"] = (
            aws_sdk_geo_routes.types.route_turn_step_details.serialize_json(
                value["turn_step_details"]
            )
        )
    import aws_sdk_geo_routes.types.route_vehicle_travel_step_type

    out["Type"] = (
        aws_sdk_geo_routes.types.route_vehicle_travel_step_type.serialize_json(
            value["type"]
        )
    )
    if "u_turn_step_details" in value:
        import aws_sdk_geo_routes.types.route_u_turn_step_details

        out["UTurnStepDetails"] = (
            aws_sdk_geo_routes.types.route_u_turn_step_details.serialize_json(
                value["u_turn_step_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleTravelStep:
    out: RouteVehicleTravelStep = {}  # type: ignore[typeddict-item]
    if "ContinueHighwayStepDetails" in data:
        import aws_sdk_geo_routes.types.route_continue_highway_step_details

        out["continue_highway_step_details"] = (
            aws_sdk_geo_routes.types.route_continue_highway_step_details.deserialize_json(
                data["ContinueHighwayStepDetails"]
            )
        )
    if "ContinueStepDetails" in data:
        import aws_sdk_geo_routes.types.route_continue_step_details

        out["continue_step_details"] = (
            aws_sdk_geo_routes.types.route_continue_step_details.deserialize_json(
                data["ContinueStepDetails"]
            )
        )
    if "CurrentRoad" in data:
        import aws_sdk_geo_routes.types.route_road

        out["current_road"] = aws_sdk_geo_routes.types.route_road.deserialize_json(
            data["CurrentRoad"]
        )
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "EnterHighwayStepDetails" in data:
        import aws_sdk_geo_routes.types.route_enter_highway_step_details

        out["enter_highway_step_details"] = (
            aws_sdk_geo_routes.types.route_enter_highway_step_details.deserialize_json(
                data["EnterHighwayStepDetails"]
            )
        )
    if "ExitNumber" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["exit_number"] = (
            aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
                data["ExitNumber"]
            )
        )
    if "ExitStepDetails" in data:
        import aws_sdk_geo_routes.types.route_exit_step_details

        out["exit_step_details"] = (
            aws_sdk_geo_routes.types.route_exit_step_details.deserialize_json(
                data["ExitStepDetails"]
            )
        )
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    if "Instruction" in data:
        out["instruction"] = data["Instruction"]
    if "KeepStepDetails" in data:
        import aws_sdk_geo_routes.types.route_keep_step_details

        out["keep_step_details"] = (
            aws_sdk_geo_routes.types.route_keep_step_details.deserialize_json(
                data["KeepStepDetails"]
            )
        )
    if "NextRoad" in data:
        import aws_sdk_geo_routes.types.route_road

        out["next_road"] = aws_sdk_geo_routes.types.route_road.deserialize_json(
            data["NextRoad"]
        )
    if "RampStepDetails" in data:
        import aws_sdk_geo_routes.types.route_ramp_step_details

        out["ramp_step_details"] = (
            aws_sdk_geo_routes.types.route_ramp_step_details.deserialize_json(
                data["RampStepDetails"]
            )
        )
    if "RoundaboutEnterStepDetails" in data:
        import aws_sdk_geo_routes.types.route_roundabout_enter_step_details

        out["roundabout_enter_step_details"] = (
            aws_sdk_geo_routes.types.route_roundabout_enter_step_details.deserialize_json(
                data["RoundaboutEnterStepDetails"]
            )
        )
    if "RoundaboutExitStepDetails" in data:
        import aws_sdk_geo_routes.types.route_roundabout_exit_step_details

        out["roundabout_exit_step_details"] = (
            aws_sdk_geo_routes.types.route_roundabout_exit_step_details.deserialize_json(
                data["RoundaboutExitStepDetails"]
            )
        )
    if "RoundaboutPassStepDetails" in data:
        import aws_sdk_geo_routes.types.route_roundabout_pass_step_details

        out["roundabout_pass_step_details"] = (
            aws_sdk_geo_routes.types.route_roundabout_pass_step_details.deserialize_json(
                data["RoundaboutPassStepDetails"]
            )
        )
    if "Signpost" in data:
        import aws_sdk_geo_routes.types.route_signpost

        out["signpost"] = aws_sdk_geo_routes.types.route_signpost.deserialize_json(
            data["Signpost"]
        )
    if "TurnStepDetails" in data:
        import aws_sdk_geo_routes.types.route_turn_step_details

        out["turn_step_details"] = (
            aws_sdk_geo_routes.types.route_turn_step_details.deserialize_json(
                data["TurnStepDetails"]
            )
        )
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_vehicle_travel_step_type

        out["type"] = (
            aws_sdk_geo_routes.types.route_vehicle_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleTravelStep.type required")
    if "UTurnStepDetails" in data:
        import aws_sdk_geo_routes.types.route_u_turn_step_details

        out["u_turn_step_details"] = (
            aws_sdk_geo_routes.types.route_u_turn_step_details.deserialize_json(
                data["UTurnStepDetails"]
            )
        )
    return out
