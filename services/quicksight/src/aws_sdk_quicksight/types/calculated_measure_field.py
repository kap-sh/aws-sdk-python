"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedMeasureField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.expression
    import aws_sdk_quicksight.types.field_id


class CalculatedMeasureField(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    expression: "aws_sdk_quicksight.types.expression.Expression"
    """<p>The expression in the table calculation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedMeasureField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> CalculatedMeasureField:
    out: CalculatedMeasureField = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("CalculatedMeasureField.field_id required")
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("CalculatedMeasureField.expression required")
    return out
