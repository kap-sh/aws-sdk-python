"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteExitStepDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.localized_string_list
    import aws_sdk_geo_routes.types.route_steering_direction
    import aws_sdk_geo_routes.types.route_turn_intensity
    import aws_sdk_geo_routes.types.sensitive_integer
    import aws_sdk_geo_routes.types.turn_angle


class RouteExitStepDetails(TypedDict, closed=True):
    intersection: "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the intersection, if applicable to the step.</p>"""
    relative_exit: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Exit to be taken.</p>"""
    steering_direction: NotRequired[
        "aws_sdk_geo_routes.types.route_steering_direction.RouteSteeringDirection"
    ]
    """<p>Steering direction for the step.</p>"""
    turn_angle: "aws_sdk_geo_routes.types.turn_angle.TurnAngle"
    """<p>Angle of the turn.</p>"""
    turn_intensity: NotRequired[
        "aws_sdk_geo_routes.types.route_turn_intensity.RouteTurnIntensity"
    ]
    """<p>Intensity of the turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteExitStepDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.localized_string_list

    out["Intersection"] = aws_sdk_geo_routes.types.localized_string_list.serialize_json(
        value["intersection"]
    )
    if "relative_exit" in value:
        out["RelativeExit"] = value["relative_exit"]
    if "steering_direction" in value:
        import aws_sdk_geo_routes.types.route_steering_direction

        out["SteeringDirection"] = (
            aws_sdk_geo_routes.types.route_steering_direction.serialize_json(
                value["steering_direction"]
            )
        )
    out["TurnAngle"] = value.get("turn_angle", 0)
    if "turn_intensity" in value:
        import aws_sdk_geo_routes.types.route_turn_intensity

        out["TurnIntensity"] = (
            aws_sdk_geo_routes.types.route_turn_intensity.serialize_json(
                value["turn_intensity"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteExitStepDetails:
    out: RouteExitStepDetails = {}  # type: ignore[typeddict-item]
    if "Intersection" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["intersection"] = (
            aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
                data["Intersection"]
            )
        )
    else:
        raise DeserializationError("RouteExitStepDetails.intersection required")
    if "RelativeExit" in data:
        out["relative_exit"] = data["RelativeExit"]
    if "SteeringDirection" in data:
        import aws_sdk_geo_routes.types.route_steering_direction

        out["steering_direction"] = (
            aws_sdk_geo_routes.types.route_steering_direction.deserialize_json(
                data["SteeringDirection"]
            )
        )
    if "TurnAngle" in data:
        out["turn_angle"] = data["TurnAngle"]
    else:
        out["turn_angle"] = 0
    if "TurnIntensity" in data:
        import aws_sdk_geo_routes.types.route_turn_intensity

        out["turn_intensity"] = (
            aws_sdk_geo_routes.types.route_turn_intensity.deserialize_json(
                data["TurnIntensity"]
            )
        )
    return out
