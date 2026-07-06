"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.non_empty_string


class DataSetReference(TypedDict, closed=True):
    data_set_placeholder: "aws_sdk_quicksight.types.non_empty_string.NonEmptyString"
    """<p>Dataset placeholder.</p>"""
    data_set_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>Dataset Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetReference) -> dict:
    out: dict = {}
    out["DataSetPlaceholder"] = value["data_set_placeholder"]
    out["DataSetArn"] = value["data_set_arn"]
    return out


def deserialize_json(data: dict) -> DataSetReference:
    out: DataSetReference = {}  # type: ignore[typeddict-item]
    if "DataSetPlaceholder" in data:
        out["data_set_placeholder"] = data["DataSetPlaceholder"]
    else:
        raise DeserializationError("DataSetReference.data_set_placeholder required")
    if "DataSetArn" in data:
        out["data_set_arn"] = data["DataSetArn"]
    else:
        raise DeserializationError("DataSetReference.data_set_arn required")
    return out
