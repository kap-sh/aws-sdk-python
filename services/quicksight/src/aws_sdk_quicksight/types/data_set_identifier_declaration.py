"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetIdentifierDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_set_identifier


class DataSetIdentifierDeclaration(TypedDict, closed=True):
    identifier: "aws_sdk_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>The identifier of the data set, typically the data set's name.</p>"""
    data_set_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetIdentifierDeclaration) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    out["DataSetArn"] = value["data_set_arn"]
    return out


def deserialize_json(data: dict) -> DataSetIdentifierDeclaration:
    out: DataSetIdentifierDeclaration = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("DataSetIdentifierDeclaration.identifier required")
    if "DataSetArn" in data:
        out["data_set_arn"] = data["DataSetArn"]
    else:
        raise DeserializationError("DataSetIdentifierDeclaration.data_set_arn required")
    return out
