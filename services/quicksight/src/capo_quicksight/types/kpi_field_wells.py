"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class KPIFieldWells(TypedDict, closed=True):
    values: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a KPI visual.</p>"""
    target_values: NotRequired[
        "capo_quicksight.types.measure_field_list.MeasureFieldList"
    ]
    """<p>The target value field wells of a KPI visual.</p>"""
    trend_groups: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The trend group field wells of a KPI visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIFieldWells) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["Values"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "target_values" in value:
        import capo_quicksight.types.measure_field_list

        out["TargetValues"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["target_values"]
        )
    if "trend_groups" in value:
        import capo_quicksight.types.dimension_field_list

        out["TrendGroups"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["trend_groups"]
        )
    return out


def deserialize_json(data: dict) -> KPIFieldWells:
    out: KPIFieldWells = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if "TargetValues" in data:
        import capo_quicksight.types.measure_field_list

        out["target_values"] = (
            capo_quicksight.types.measure_field_list.deserialize_json(
                data["TargetValues"]
            )
        )
    if "TrendGroups" in data:
        import capo_quicksight.types.dimension_field_list

        out["trend_groups"] = (
            capo_quicksight.types.dimension_field_list.deserialize_json(
                data["TrendGroups"]
            )
        )
    return out
