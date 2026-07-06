"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTravelStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_continue_step_details
    import aws_sdk_geo_routes.types.route_exit_step_details
    import aws_sdk_geo_routes.types.route_keep_step_details
    import aws_sdk_geo_routes.types.route_ramp_step_details
    import aws_sdk_geo_routes.types.route_roundabout_enter_step_details
    import aws_sdk_geo_routes.types.route_roundabout_exit_step_details
    import aws_sdk_geo_routes.types.route_roundabout_pass_step_details
    import aws_sdk_geo_routes.types.route_taxi_travel_step_type
    import aws_sdk_geo_routes.types.route_turn_step_details
    import aws_sdk_geo_routes.types.route_u_turn_step_details
    import aws_sdk_geo_routes.types.sensitive_string


class RouteTaxiTravelStep(TypedDict, closed=True):
    continue_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_continue_step_details.RouteContinueStepDetails"
    ]
    distance: NotRequired["aws_sdk_geo_routes.types.distance_meters.DistanceMeters"]
    """<p>Distance of the step.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    exit_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_exit_step_details.RouteExitStepDetails"
    ]
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    instruction: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Brief description of the step in the requested language.</p>"""
    keep_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_keep_step_details.RouteKeepStepDetails"
    ]
    ramp_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_ramp_step_details.RouteRampStepDetails"
    ]
    roundabout_enter_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_roundabout_enter_step_details.RouteRoundaboutEnterStepDetails"
    ]
    roundabout_exit_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_roundabout_exit_step_details.RouteRoundaboutExitStepDetails"
    ]
    roundabout_pass_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_roundabout_pass_step_details.RouteRoundaboutPassStepDetails"
    ]
    turn_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_turn_step_details.RouteTurnStepDetails"
    ]
    type: "aws_sdk_geo_routes.types.route_taxi_travel_step_type.RouteTaxiTravelStepType"
    """<p>Type of the step.</p>"""
    u_turn_step_details: NotRequired[
        "aws_sdk_geo_routes.types.route_u_turn_step_details.RouteUTurnStepDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiTravelStep) -> dict:
    out: dict = {}
    if "continue_step_details" in value:
        import aws_sdk_geo_routes.types.route_continue_step_details

        out["ContinueStepDetails"] = (
            aws_sdk_geo_routes.types.route_continue_step_details.serialize_json(
                value["continue_step_details"]
            )
        )
    if "distance" in value:
        out["Distance"] = value["distance"]
    out["Duration"] = value["duration"]
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
    if "turn_step_details" in value:
        import aws_sdk_geo_routes.types.route_turn_step_details

        out["TurnStepDetails"] = (
            aws_sdk_geo_routes.types.route_turn_step_details.serialize_json(
                value["turn_step_details"]
            )
        )
    import aws_sdk_geo_routes.types.route_taxi_travel_step_type

    out["Type"] = aws_sdk_geo_routes.types.route_taxi_travel_step_type.serialize_json(
        value["type"]
    )
    if "u_turn_step_details" in value:
        import aws_sdk_geo_routes.types.route_u_turn_step_details

        out["UTurnStepDetails"] = (
            aws_sdk_geo_routes.types.route_u_turn_step_details.serialize_json(
                value["u_turn_step_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTaxiTravelStep:
    out: RouteTaxiTravelStep = {}  # type: ignore[typeddict-item]
    if "ContinueStepDetails" in data:
        import aws_sdk_geo_routes.types.route_continue_step_details

        out["continue_step_details"] = (
            aws_sdk_geo_routes.types.route_continue_step_details.deserialize_json(
                data["ContinueStepDetails"]
            )
        )
    if "Distance" in data:
        out["distance"] = data["Distance"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTaxiTravelStep.duration required")
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
    if "TurnStepDetails" in data:
        import aws_sdk_geo_routes.types.route_turn_step_details

        out["turn_step_details"] = (
            aws_sdk_geo_routes.types.route_turn_step_details.deserialize_json(
                data["TurnStepDetails"]
            )
        )
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_taxi_travel_step_type

        out["type"] = (
            aws_sdk_geo_routes.types.route_taxi_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiTravelStep.type required")
    if "UTurnStepDetails" in data:
        import aws_sdk_geo_routes.types.route_u_turn_step_details

        out["u_turn_step_details"] = (
            aws_sdk_geo_routes.types.route_u_turn_step_details.deserialize_json(
                data["UTurnStepDetails"]
            )
        )
    return out
