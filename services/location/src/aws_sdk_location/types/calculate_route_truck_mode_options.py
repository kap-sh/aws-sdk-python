"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteTruckModeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.sensitive_boolean
    import aws_sdk_location.types.truck_dimensions
    import aws_sdk_location.types.truck_weight


class CalculateRouteTruckModeOptions(TypedDict, closed=True):
    avoid_ferries: NotRequired[
        "aws_sdk_location.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoids ferries when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    avoid_tolls: NotRequired[
        "aws_sdk_location.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoids tolls when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    dimensions: NotRequired["aws_sdk_location.types.truck_dimensions.TruckDimensions"]
    """<p>Specifies the truck's dimension specifications including length, height, width, and unit of measurement. Used to avoid roads that can't support the truck's dimensions.</p>"""
    weight: NotRequired["aws_sdk_location.types.truck_weight.TruckWeight"]
    """<p>Specifies the truck's weight specifications including total weight and unit of measurement. Used to avoid roads that can't support the truck's weight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteTruckModeOptions) -> dict:
    out: dict = {}
    if "avoid_ferries" in value:
        out["AvoidFerries"] = value["avoid_ferries"]
    if "avoid_tolls" in value:
        out["AvoidTolls"] = value["avoid_tolls"]
    if "dimensions" in value:
        import aws_sdk_location.types.truck_dimensions

        out["Dimensions"] = aws_sdk_location.types.truck_dimensions.serialize_json(
            value["dimensions"]
        )
    if "weight" in value:
        import aws_sdk_location.types.truck_weight

        out["Weight"] = aws_sdk_location.types.truck_weight.serialize_json(
            value["weight"]
        )
    return out


def deserialize_json(data: dict) -> CalculateRouteTruckModeOptions:
    out: CalculateRouteTruckModeOptions = {}  # type: ignore[typeddict-item]
    if "AvoidFerries" in data:
        out["avoid_ferries"] = data["AvoidFerries"]
    if "AvoidTolls" in data:
        out["avoid_tolls"] = data["AvoidTolls"]
    if "Dimensions" in data:
        import aws_sdk_location.types.truck_dimensions

        out["dimensions"] = aws_sdk_location.types.truck_dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "Weight" in data:
        import aws_sdk_location.types.truck_weight

        out["weight"] = aws_sdk_location.types.truck_weight.deserialize_json(
            data["Weight"]
        )
    return out
