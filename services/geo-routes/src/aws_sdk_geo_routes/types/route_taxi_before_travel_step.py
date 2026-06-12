"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiBeforeTravelStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_taxi_before_travel_step_type
    import aws_sdk_geo_routes.types.sensitive_string


class RouteTaxiBeforeTravelStep(TypedDict):
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    instruction: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Brief description of the step in the requested language.</p>"""
    type: "aws_sdk_geo_routes.types.route_taxi_before_travel_step_type.RouteTaxiBeforeTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiBeforeTravelStep) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import aws_sdk_geo_routes.types.route_taxi_before_travel_step_type

    out["Type"] = (
        aws_sdk_geo_routes.types.route_taxi_before_travel_step_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteTaxiBeforeTravelStep:
    out: RouteTaxiBeforeTravelStep = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTaxiBeforeTravelStep.duration required")
    if "Instruction" in data:
        out["instruction"] = data["Instruction"]
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_taxi_before_travel_step_type

        out["type"] = (
            aws_sdk_geo_routes.types.route_taxi_before_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiBeforeTravelStep.type required")
    return out
