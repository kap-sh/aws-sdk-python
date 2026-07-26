"""Generated from Smithy shape ``com.amazonaws.quicksight#SourceTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id
    import capo_quicksight.types.parent_data_set


class SourceTable(TypedDict, closed=True):
    physical_table_id: NotRequired[
        "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    ]
    """<p>The identifier of the physical table that serves as the data source.</p>"""
    data_set: NotRequired["capo_quicksight.types.parent_data_set.ParentDataSet"]
    """<p>A parent dataset that serves as the data source instead of a physical table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceTable) -> dict:
    out: dict = {}
    if "physical_table_id" in value:
        out["PhysicalTableId"] = value["physical_table_id"]
    if "data_set" in value:
        import capo_quicksight.types.parent_data_set

        out["DataSet"] = capo_quicksight.types.parent_data_set.serialize_json(
            value["data_set"]
        )
    return out


def deserialize_json(data: dict) -> SourceTable:
    out: SourceTable = {}  # type: ignore[typeddict-item]
    if "PhysicalTableId" in data:
        out["physical_table_id"] = data["PhysicalTableId"]
    if "DataSet" in data:
        import capo_quicksight.types.parent_data_set

        out["data_set"] = capo_quicksight.types.parent_data_set.deserialize_json(
            data["DataSet"]
        )
    return out
