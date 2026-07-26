"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianTravelStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.localized_string_list
    import capo_geo_routes.types.route_continue_step_details
    import capo_geo_routes.types.route_keep_step_details
    import capo_geo_routes.types.route_pedestrian_travel_step_type
    import capo_geo_routes.types.route_road
    import capo_geo_routes.types.route_roundabout_enter_step_details
    import capo_geo_routes.types.route_roundabout_exit_step_details
    import capo_geo_routes.types.route_roundabout_pass_step_details
    import capo_geo_routes.types.route_signpost
    import capo_geo_routes.types.route_turn_step_details
    import capo_geo_routes.types.sensitive_string


class RoutePedestrianTravelStep(TypedDict, closed=True):
    continue_step_details: NotRequired[
        "capo_geo_routes.types.route_continue_step_details.RouteContinueStepDetails"
    ]
    """<p>Details related to the continue step.</p>"""
    current_road: NotRequired["capo_geo_routes.types.route_road.RouteRoad"]
    """<p>Details of the current road. See RouteRoad for details of sub-attributes.</p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the step.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    exit_number: NotRequired[
        "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    ]
    """<p>Exit number of the road exit, if applicable.</p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p> <note> <p>Only available when the TravelStepType is Default.</p> </note>"""
    keep_step_details: NotRequired[
        "capo_geo_routes.types.route_keep_step_details.RouteKeepStepDetails"
    ]
    """<p>Details that are specific to a Keep step.</p>"""
    next_road: NotRequired["capo_geo_routes.types.route_road.RouteRoad"]
    """<p>Details of the next road. See RouteRoad for details of sub-attributes.</p>"""
    roundabout_enter_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_enter_step_details.RouteRoundaboutEnterStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Enter step.</p>"""
    roundabout_exit_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_exit_step_details.RouteRoundaboutExitStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Exit step.</p>"""
    roundabout_pass_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_pass_step_details.RouteRoundaboutPassStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Pass step.</p>"""
    signpost: NotRequired["capo_geo_routes.types.route_signpost.RouteSignpost"]
    """<p>Sign post information of the action, applicable only for TurnByTurn steps. See RouteSignpost for details of sub-attributes.</p>"""
    turn_step_details: NotRequired[
        "capo_geo_routes.types.route_turn_step_details.RouteTurnStepDetails"
    ]
    """<p>Details that are specific to a turn step.</p>"""
    type: "capo_geo_routes.types.route_pedestrian_travel_step_type.RoutePedestrianTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianTravelStep) -> dict:
    out: dict = {}
    if "continue_step_details" in value:
        import capo_geo_routes.types.route_continue_step_details

        out["ContinueStepDetails"] = (
            capo_geo_routes.types.route_continue_step_details.serialize_json(
                value["continue_step_details"]
            )
        )
    if "current_road" in value:
        import capo_geo_routes.types.route_road

        out["CurrentRoad"] = capo_geo_routes.types.route_road.serialize_json(
            value["current_road"]
        )
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "exit_number" in value:
        import capo_geo_routes.types.localized_string_list

        out["ExitNumber"] = capo_geo_routes.types.localized_string_list.serialize_json(
            value["exit_number"]
        )
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    if "keep_step_details" in value:
        import capo_geo_routes.types.route_keep_step_details

        out["KeepStepDetails"] = (
            capo_geo_routes.types.route_keep_step_details.serialize_json(
                value["keep_step_details"]
            )
        )
    if "next_road" in value:
        import capo_geo_routes.types.route_road

        out["NextRoad"] = capo_geo_routes.types.route_road.serialize_json(
            value["next_road"]
        )
    if "roundabout_enter_step_details" in value:
        import capo_geo_routes.types.route_roundabout_enter_step_details

        out["RoundaboutEnterStepDetails"] = (
            capo_geo_routes.types.route_roundabout_enter_step_details.serialize_json(
                value["roundabout_enter_step_details"]
            )
        )
    if "roundabout_exit_step_details" in value:
        import capo_geo_routes.types.route_roundabout_exit_step_details

        out["RoundaboutExitStepDetails"] = (
            capo_geo_routes.types.route_roundabout_exit_step_details.serialize_json(
                value["roundabout_exit_step_details"]
            )
        )
    if "roundabout_pass_step_details" in value:
        import capo_geo_routes.types.route_roundabout_pass_step_details

        out["RoundaboutPassStepDetails"] = (
            capo_geo_routes.types.route_roundabout_pass_step_details.serialize_json(
                value["roundabout_pass_step_details"]
            )
        )
    if "signpost" in value:
        import capo_geo_routes.types.route_signpost

        out["Signpost"] = capo_geo_routes.types.route_signpost.serialize_json(
            value["signpost"]
        )
    if "turn_step_details" in value:
        import capo_geo_routes.types.route_turn_step_details

        out["TurnStepDetails"] = (
            capo_geo_routes.types.route_turn_step_details.serialize_json(
                value["turn_step_details"]
            )
        )
    import capo_geo_routes.types.route_pedestrian_travel_step_type

    out["Type"] = (
        capo_geo_routes.types.route_pedestrian_travel_step_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RoutePedestrianTravelStep:
    out: RoutePedestrianTravelStep = {}  # type: ignore[typeddict-item]
    if "ContinueStepDetails" in data:
        import capo_geo_routes.types.route_continue_step_details

        out["continue_step_details"] = (
            capo_geo_routes.types.route_continue_step_details.deserialize_json(
                data["ContinueStepDetails"]
            )
        )
    if "CurrentRoad" in data:
        import capo_geo_routes.types.route_road

        out["current_road"] = capo_geo_routes.types.route_road.deserialize_json(
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
    if "ExitNumber" in data:
        import capo_geo_routes.types.localized_string_list

        out["exit_number"] = (
            capo_geo_routes.types.localized_string_list.deserialize_json(
                data["ExitNumber"]
            )
        )
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    if "Instruction" in data:
        out["instruction"] = data["Instruction"]
    if "KeepStepDetails" in data:
        import capo_geo_routes.types.route_keep_step_details

        out["keep_step_details"] = (
            capo_geo_routes.types.route_keep_step_details.deserialize_json(
                data["KeepStepDetails"]
            )
        )
    if "NextRoad" in data:
        import capo_geo_routes.types.route_road

        out["next_road"] = capo_geo_routes.types.route_road.deserialize_json(
            data["NextRoad"]
        )
    if "RoundaboutEnterStepDetails" in data:
        import capo_geo_routes.types.route_roundabout_enter_step_details

        out["roundabout_enter_step_details"] = (
            capo_geo_routes.types.route_roundabout_enter_step_details.deserialize_json(
                data["RoundaboutEnterStepDetails"]
            )
        )
    if "RoundaboutExitStepDetails" in data:
        import capo_geo_routes.types.route_roundabout_exit_step_details

        out["roundabout_exit_step_details"] = (
            capo_geo_routes.types.route_roundabout_exit_step_details.deserialize_json(
                data["RoundaboutExitStepDetails"]
            )
        )
    if "RoundaboutPassStepDetails" in data:
        import capo_geo_routes.types.route_roundabout_pass_step_details

        out["roundabout_pass_step_details"] = (
            capo_geo_routes.types.route_roundabout_pass_step_details.deserialize_json(
                data["RoundaboutPassStepDetails"]
            )
        )
    if "Signpost" in data:
        import capo_geo_routes.types.route_signpost

        out["signpost"] = capo_geo_routes.types.route_signpost.deserialize_json(
            data["Signpost"]
        )
    if "TurnStepDetails" in data:
        import capo_geo_routes.types.route_turn_step_details

        out["turn_step_details"] = (
            capo_geo_routes.types.route_turn_step_details.deserialize_json(
                data["TurnStepDetails"]
            )
        )
    if "Type" in data:
        import capo_geo_routes.types.route_pedestrian_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_pedestrian_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianTravelStep.type required")
    return out
