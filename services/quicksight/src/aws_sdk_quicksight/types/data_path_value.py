"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_path_type
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.field_value


class DataPathValue(TypedDict, closed=True):
    field_id: NotRequired["aws_sdk_quicksight.types.field_id.FieldId"]
    """<p>The field ID of the field that needs to be sorted.</p>"""
    field_value: NotRequired["aws_sdk_quicksight.types.field_value.FieldValue"]
    """<p>The actual value of the field that needs to be sorted.</p>"""
    data_path_type: NotRequired["aws_sdk_quicksight.types.data_path_type.DataPathType"]
    """<p>The type configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPathValue) -> dict:
    out: dict = {}
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    if "data_path_type" in value:
        import aws_sdk_quicksight.types.data_path_type

        out["DataPathType"] = aws_sdk_quicksight.types.data_path_type.serialize_json(
            value["data_path_type"]
        )
    return out


def deserialize_json(data: dict) -> DataPathValue:
    out: DataPathValue = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    if "FieldValue" in data:
        out["field_value"] = data["FieldValue"]
    if "DataPathType" in data:
        import aws_sdk_quicksight.types.data_path_type

        out["data_path_type"] = (
            aws_sdk_quicksight.types.data_path_type.deserialize_json(
                data["DataPathType"]
            )
        )
    return out
