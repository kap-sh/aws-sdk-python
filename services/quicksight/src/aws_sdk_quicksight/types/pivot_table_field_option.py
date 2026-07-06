"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_label
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.visibility


class PivotTableFieldOption(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID of the pivot table field.</p>"""
    custom_label: NotRequired["aws_sdk_quicksight.types.custom_label.CustomLabel"]
    """<p>The custom label of the pivot table field.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the pivot table field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldOption) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldOption:
    out: PivotTableFieldOption = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("PivotTableFieldOption.field_id required")
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
