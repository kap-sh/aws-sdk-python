"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldSubtotalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id


class PivotTableFieldSubtotalOptions(TypedDict, closed=True):
    field_id: NotRequired["aws_sdk_quicksight.types.field_id.FieldId"]
    """<p>The field ID of the subtotal options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldSubtotalOptions) -> dict:
    out: dict = {}
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    return out


def deserialize_json(data: dict) -> PivotTableFieldSubtotalOptions:
    out: PivotTableFieldSubtotalOptions = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    return out
