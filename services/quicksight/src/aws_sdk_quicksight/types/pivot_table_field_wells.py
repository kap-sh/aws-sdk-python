"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_aggregated_field_wells


class PivotTableFieldWells(TypedDict):
    pivot_table_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_aggregated_field_wells.PivotTableAggregatedFieldWells"
    ]
    """<p>The aggregated field well for the pivot table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldWells) -> dict:
    out: dict = {}
    if "pivot_table_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.pivot_table_aggregated_field_wells

        out["PivotTableAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.pivot_table_aggregated_field_wells.serialize_json(
                value["pivot_table_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldWells:
    out: PivotTableFieldWells = {}  # type: ignore[typeddict-item]
    if "PivotTableAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.pivot_table_aggregated_field_wells

        out["pivot_table_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.pivot_table_aggregated_field_wells.deserialize_json(
                data["PivotTableAggregatedFieldWells"]
            )
        )
    return out
