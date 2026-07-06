"""Generated from Smithy shape ``com.amazonaws.quicksight#TableUnaggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_unaggregated_field_list


class TableUnaggregatedFieldWells(TypedDict, closed=True):
    values: NotRequired[
        "aws_sdk_quicksight.types.table_unaggregated_field_list.TableUnaggregatedFieldList"
    ]
    """<p>The values field well for a pivot table. Values are unaggregated for an unaggregated table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableUnaggregatedFieldWells) -> dict:
    out: dict = {}
    if "values" in value:
        import aws_sdk_quicksight.types.table_unaggregated_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.table_unaggregated_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableUnaggregatedFieldWells:
    out: TableUnaggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_quicksight.types.table_unaggregated_field_list

        out["values"] = (
            aws_sdk_quicksight.types.table_unaggregated_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
