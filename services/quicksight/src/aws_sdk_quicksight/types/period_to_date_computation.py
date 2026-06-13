"""Generated from Smithy shape ``com.amazonaws.quicksight#PeriodToDateComputation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field
    import aws_sdk_quicksight.types.measure_field
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.time_granularity


class PeriodToDateComputation(TypedDict):
    computation_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for a computation.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["aws_sdk_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    value: NotRequired["aws_sdk_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    period_time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity setup of period to date computation. Choose from the following options:</p> <ul> <li> <p>YEAR: Year to date.</p> </li> <li> <p>MONTH: Month to date.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PeriodToDateComputation) -> dict:
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
    if "period_time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["PeriodTimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["period_time_granularity"]
            )
        )
    return out


def deserialize_json(data: dict) -> PeriodToDateComputation:
    out: PeriodToDateComputation = {}  # type: ignore[typeddict-item]
    if "ComputationId" in data:
        out["computation_id"] = data["ComputationId"]
    else:
        raise DeserializationError("PeriodToDateComputation.computation_id required")
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
    if "PeriodTimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["period_time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["PeriodTimeGranularity"]
            )
        )
    return out
