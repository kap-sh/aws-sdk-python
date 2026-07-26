"""Generated from Smithy shape ``com.amazonaws.quicksight#ParentDataSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.input_column_list


class ParentDataSet(TypedDict, closed=True):
    data_set_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the parent dataset.</p>"""
    input_columns: "capo_quicksight.types.input_column_list.InputColumnList"
    """<p>The list of input columns available from the parent dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentDataSet) -> dict:
    out: dict = {}
    out["DataSetArn"] = value["data_set_arn"]
    import capo_quicksight.types.input_column_list

    out["InputColumns"] = capo_quicksight.types.input_column_list.serialize_json(
        value["input_columns"]
    )
    return out


def deserialize_json(data: dict) -> ParentDataSet:
    out: ParentDataSet = {}  # type: ignore[typeddict-item]
    if "DataSetArn" in data:
        out["data_set_arn"] = data["DataSetArn"]
    else:
        raise DeserializationError("ParentDataSet.data_set_arn required")
    if "InputColumns" in data:
        import capo_quicksight.types.input_column_list

        out["input_columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["InputColumns"]
        )
    else:
        raise DeserializationError("ParentDataSet.input_columns required")
    return out
