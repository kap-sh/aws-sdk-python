"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldLabelType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.visibility


class FieldLabelType(TypedDict):
    field_id: NotRequired["aws_sdk_quicksight.types.field_id.FieldId"]
    """<p>Indicates the field that is targeted by the field label.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the field label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldLabelType) -> dict:
    out: dict = {}
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> FieldLabelType:
    out: FieldLabelType = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
