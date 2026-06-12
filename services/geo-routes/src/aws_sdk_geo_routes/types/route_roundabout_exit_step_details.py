"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRoundaboutExitStepDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.localized_string_list
    import aws_sdk_geo_routes.types.roundabout_angle
    import aws_sdk_geo_routes.types.route_steering_direction
    import aws_sdk_geo_routes.types.sensitive_integer


class RouteRoundaboutExitStepDetails(TypedDict):
    intersection: "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the intersection, if applicable to the step.</p>"""
    relative_exit: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Exit to be taken.</p>"""
    roundabout_angle: "aws_sdk_geo_routes.types.roundabout_angle.RoundaboutAngle"
    """<p>Angle of the roundabout.</p>"""
    steering_direction: NotRequired[
        "aws_sdk_geo_routes.types.route_steering_direction.RouteSteeringDirection"
    ]
    """<p>Steering direction for the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRoundaboutExitStepDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.localized_string_list

    out["Intersection"] = aws_sdk_geo_routes.types.localized_string_list.serialize_json(
        value["intersection"]
    )
    if "relative_exit" in value:
        out["RelativeExit"] = value["relative_exit"]
    out["RoundaboutAngle"] = value.get("roundabout_angle", 0)
    if "steering_direction" in value:
        import aws_sdk_geo_routes.types.route_steering_direction

        out["SteeringDirection"] = (
            aws_sdk_geo_routes.types.route_steering_direction.serialize_json(
                value["steering_direction"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteRoundaboutExitStepDetails:
    out: RouteRoundaboutExitStepDetails = {}  # type: ignore[typeddict-item]
    if "Intersection" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["intersection"] = (
            aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
                data["Intersection"]
            )
        )
    else:
        raise DeserializationError(
            "RouteRoundaboutExitStepDetails.intersection required"
        )
    if "RelativeExit" in data:
        out["relative_exit"] = data["RelativeExit"]
    if "RoundaboutAngle" in data:
        out["roundabout_angle"] = data["RoundaboutAngle"]
    else:
        out["roundabout_angle"] = 0
    if "SteeringDirection" in data:
        import aws_sdk_geo_routes.types.route_steering_direction

        out["steering_direction"] = (
            aws_sdk_geo_routes.types.route_steering_direction.deserialize_json(
                data["SteeringDirection"]
            )
        )
    return out
