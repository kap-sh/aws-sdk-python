"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Csv``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.column_names


class Csv(TypedDict, closed=True):
    column_names: "aws_sdk_iotsitewise.types.column_names.ColumnNames"
    """<p>The column names specified in the .csv file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Csv) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.column_names

    out["columnNames"] = aws_sdk_iotsitewise.types.column_names.serialize_json(
        value["column_names"]
    )
    return out


def deserialize_json(data: dict) -> Csv:
    out: Csv = {}  # type: ignore[typeddict-item]
    if "columnNames" in data:
        import aws_sdk_iotsitewise.types.column_names

        out["column_names"] = aws_sdk_iotsitewise.types.column_names.deserialize_json(
            data["columnNames"]
        )
    else:
        raise DeserializationError("Csv.column_names required")
    return out
