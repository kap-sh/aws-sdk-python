"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepListAggregationFunction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.separator


class DataPrepListAggregationFunction(TypedDict):
    input_column_name: NotRequired["aws_sdk_quicksight.types.column_name.ColumnName"]
    """<p>The name of the column containing values to be concatenated.</p>"""
    separator: "aws_sdk_quicksight.types.separator.Separator"
    """<p>The string used to separate values in the concatenated result.</p>"""
    distinct: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>Whether to include only distinct values in the concatenated result, removing duplicates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrepListAggregationFunction) -> dict:
    out: dict = {}
    if "input_column_name" in value:
        out["InputColumnName"] = value["input_column_name"]
    out["Separator"] = value["separator"]
    out["Distinct"] = value.get("distinct", False)
    return out


def deserialize_json(data: dict) -> DataPrepListAggregationFunction:
    out: DataPrepListAggregationFunction = {}  # type: ignore[typeddict-item]
    if "InputColumnName" in data:
        out["input_column_name"] = data["InputColumnName"]
    if "Separator" in data:
        out["separator"] = data["Separator"]
    else:
        raise DeserializationError("DataPrepListAggregationFunction.separator required")
    if "Distinct" in data:
        out["distinct"] = data["Distinct"]
    else:
        out["distinct"] = False
    return out
