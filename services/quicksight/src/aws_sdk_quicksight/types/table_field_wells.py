"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_aggregated_field_wells
    import aws_sdk_quicksight.types.table_unaggregated_field_wells


class TableFieldWells(TypedDict):
    table_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.table_aggregated_field_wells.TableAggregatedFieldWells"
    ]
    """<p>The aggregated field well for the table.</p>"""
    table_unaggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.table_unaggregated_field_wells.TableUnaggregatedFieldWells"
    ]
    """<p>The unaggregated field well for the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldWells) -> dict:
    out: dict = {}
    if "table_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.table_aggregated_field_wells

        out["TableAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.table_aggregated_field_wells.serialize_json(
                value["table_aggregated_field_wells"]
            )
        )
    if "table_unaggregated_field_wells" in value:
        import aws_sdk_quicksight.types.table_unaggregated_field_wells

        out["TableUnaggregatedFieldWells"] = (
            aws_sdk_quicksight.types.table_unaggregated_field_wells.serialize_json(
                value["table_unaggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldWells:
    out: TableFieldWells = {}  # type: ignore[typeddict-item]
    if "TableAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.table_aggregated_field_wells

        out["table_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.table_aggregated_field_wells.deserialize_json(
                data["TableAggregatedFieldWells"]
            )
        )
    if "TableUnaggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.table_unaggregated_field_wells

        out["table_unaggregated_field_wells"] = (
            aws_sdk_quicksight.types.table_unaggregated_field_wells.deserialize_json(
                data["TableUnaggregatedFieldWells"]
            )
        )
    return out
