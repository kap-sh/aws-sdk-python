"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.measure_field_list


class GaugeChartFieldWells(TypedDict, closed=True):
    values: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a <code>GaugeChartVisual</code>.</p>"""
    target_values: NotRequired[
        "aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"
    ]
    """<p>The target value field wells of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartFieldWells) -> dict:
    out: dict = {}
    if "values" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["Values"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "target_values" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["TargetValues"] = (
            aws_sdk_quicksight.types.measure_field_list.serialize_json(
                value["target_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> GaugeChartFieldWells:
    out: GaugeChartFieldWells = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["values"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if "TargetValues" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["target_values"] = (
            aws_sdk_quicksight.types.measure_field_list.deserialize_json(
                data["TargetValues"]
            )
        )
    return out
