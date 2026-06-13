"""Generated from Smithy shape ``com.amazonaws.quicksight#ParentDataSet``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.input_column_list


class ParentDataSet(TypedDict):
    data_set_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the parent dataset.</p>"""
    input_columns: "aws_sdk_quicksight.types.input_column_list.InputColumnList"
    """<p>The list of input columns available from the parent dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentDataSet) -> dict:
    out: dict = {}
    out["DataSetArn"] = value["data_set_arn"]
    import aws_sdk_quicksight.types.input_column_list

    out["InputColumns"] = aws_sdk_quicksight.types.input_column_list.serialize_json(
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
        import aws_sdk_quicksight.types.input_column_list

        out["input_columns"] = (
            aws_sdk_quicksight.types.input_column_list.deserialize_json(
                data["InputColumns"]
            )
        )
    else:
        raise DeserializationError("ParentDataSet.input_columns required")
    return out
