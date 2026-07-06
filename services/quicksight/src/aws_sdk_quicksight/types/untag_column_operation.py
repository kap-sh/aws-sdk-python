"""Generated from Smithy shape ``com.amazonaws.quicksight#UntagColumnOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.column_tag_names


class UntagColumnOperation(TypedDict, closed=True):
    column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The column that this operation acts on.</p>"""
    tag_names: "aws_sdk_quicksight.types.column_tag_names.ColumnTagNames"
    """<p>The column tags to remove from this column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagColumnOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    import aws_sdk_quicksight.types.column_tag_names

    out["TagNames"] = aws_sdk_quicksight.types.column_tag_names.serialize_json(
        value["tag_names"]
    )
    return out


def deserialize_json(data: dict) -> UntagColumnOperation:
    out: UntagColumnOperation = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("UntagColumnOperation.column_name required")
    if "TagNames" in data:
        import aws_sdk_quicksight.types.column_tag_names

        out["tag_names"] = aws_sdk_quicksight.types.column_tag_names.deserialize_json(
            data["TagNames"]
        )
    else:
        raise DeserializationError("UntagColumnOperation.tag_names required")
    return out
