"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.calculated_field_expression
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.data_set_identifier


class CalculatedField(TypedDict, closed=True):
    data_set_identifier: (
        "aws_sdk_quicksight.types.data_set_identifier.DataSetIdentifier"
    )
    """<p>The data set that is used in this calculated field.</p>"""
    name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name of the calculated field.</p>"""
    expression: (
        "aws_sdk_quicksight.types.calculated_field_expression.CalculatedFieldExpression"
    )
    """<p>The expression of the calculated field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedField) -> dict:
    out: dict = {}
    out["DataSetIdentifier"] = value["data_set_identifier"]
    out["Name"] = value["name"]
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> CalculatedField:
    out: CalculatedField = {}  # type: ignore[typeddict-item]
    if "DataSetIdentifier" in data:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        raise DeserializationError("CalculatedField.data_set_identifier required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CalculatedField.name required")
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("CalculatedField.expression required")
    return out
