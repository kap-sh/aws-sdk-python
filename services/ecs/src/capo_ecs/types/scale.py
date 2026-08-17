"""Generated from Smithy shape ``com.amazonaws.ecs#Scale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.double
    import capo_ecs.types.scale_unit


class Scale(TypedDict, closed=True):
    value: "capo_ecs.types.double.Double"
    """<p>The value, specified as a percent total of a service's <code>desiredCount</code>, to scale the task set. Accepted values are numbers between 0 and 100.</p>"""
    unit: NotRequired["capo_ecs.types.scale_unit.ScaleUnit"]
    """<p>The unit of measure for the scale value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Scale) -> dict:
    out: dict = {}
    out["value"] = value.get("value", 0)
    if "unit" in value:
        import capo_ecs.types.scale_unit

        out["unit"] = capo_ecs.types.scale_unit.serialize_aws_json_1_1(value["unit"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Scale:
    out: Scale = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    if data.get("unit") is not None:
        import capo_ecs.types.scale_unit

        out["unit"] = capo_ecs.types.scale_unit.deserialize_aws_json_1_1(data["unit"])
    return out
