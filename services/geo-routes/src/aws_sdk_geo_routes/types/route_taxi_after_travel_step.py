"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiAfterTravelStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_taxi_after_travel_step_type
    import aws_sdk_geo_routes.types.sensitive_string


class RouteTaxiAfterTravelStep(TypedDict):
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    instruction: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Brief description of the step in the requested language.</p>"""
    type: "aws_sdk_geo_routes.types.route_taxi_after_travel_step_type.RouteTaxiAfterTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiAfterTravelStep) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import aws_sdk_geo_routes.types.route_taxi_after_travel_step_type

    out["Type"] = (
        aws_sdk_geo_routes.types.route_taxi_after_travel_step_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteTaxiAfterTravelStep:
    out: RouteTaxiAfterTravelStep = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTaxiAfterTravelStep.duration required")
    if "Instruction" in data:
        out["instruction"] = data["Instruction"]
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_taxi_after_travel_step_type

        out["type"] = (
            aws_sdk_geo_routes.types.route_taxi_after_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiAfterTravelStep.type required")
    return out
