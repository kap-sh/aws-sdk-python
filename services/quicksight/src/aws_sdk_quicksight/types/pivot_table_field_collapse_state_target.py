"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldCollapseStateTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_path_value_list
    import aws_sdk_quicksight.types.string


class PivotTableFieldCollapseStateTarget(TypedDict):
    field_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The field ID of the pivot table that the collapse state needs to be set to.</p>"""
    field_data_path_values: NotRequired[
        "aws_sdk_quicksight.types.data_path_value_list.DataPathValueList"
    ]
    """<p>The data path of the pivot table's header. Used to set the collapse state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldCollapseStateTarget) -> dict:
    out: dict = {}
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    if "field_data_path_values" in value:
        import aws_sdk_quicksight.types.data_path_value_list

        out["FieldDataPathValues"] = (
            aws_sdk_quicksight.types.data_path_value_list.serialize_json(
                value["field_data_path_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldCollapseStateTarget:
    out: PivotTableFieldCollapseStateTarget = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    if "FieldDataPathValues" in data:
        import aws_sdk_quicksight.types.data_path_value_list

        out["field_data_path_values"] = (
            aws_sdk_quicksight.types.data_path_value_list.deserialize_json(
                data["FieldDataPathValues"]
            )
        )
    return out
