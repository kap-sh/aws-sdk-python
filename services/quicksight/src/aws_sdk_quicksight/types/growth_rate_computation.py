"""Generated from Smithy shape ``com.amazonaws.quicksight#GrowthRateComputation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field
    import aws_sdk_quicksight.types.growth_rate_period_size
    import aws_sdk_quicksight.types.measure_field
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.string


class GrowthRateComputation(TypedDict):
    computation_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for a computation.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["aws_sdk_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    value: NotRequired["aws_sdk_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    period_size: NotRequired[
        "aws_sdk_quicksight.types.growth_rate_period_size.GrowthRatePeriodSize"
    ]
    """<p>The period size setup of a growth rate computation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrowthRateComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "time" in value:
        import aws_sdk_quicksight.types.dimension_field

        out["Time"] = aws_sdk_quicksight.types.dimension_field.serialize_json(
            value["time"]
        )
    if "value" in value:
        import aws_sdk_quicksight.types.measure_field

        out["Value"] = aws_sdk_quicksight.types.measure_field.serialize_json(
            value["value"]
        )
    if "period_size" in value:
        out["PeriodSize"] = value["period_size"]
    return out


def deserialize_json(data: dict) -> GrowthRateComputation:
    out: GrowthRateComputation = {}  # type: ignore[typeddict-item]
    if "ComputationId" in data:
        out["computation_id"] = data["ComputationId"]
    else:
        raise DeserializationError("GrowthRateComputation.computation_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Time" in data:
        import aws_sdk_quicksight.types.dimension_field

        out["time"] = aws_sdk_quicksight.types.dimension_field.deserialize_json(
            data["Time"]
        )
    if "Value" in data:
        import aws_sdk_quicksight.types.measure_field

        out["value"] = aws_sdk_quicksight.types.measure_field.deserialize_json(
            data["Value"]
        )
    if "PeriodSize" in data:
        out["period_size"] = data["PeriodSize"]
    return out
