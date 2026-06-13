"""Generated from Smithy shape ``com.amazonaws.quicksight#TagColumnOperation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.column_tag_list


class TagColumnOperation(TypedDict):
    column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The column that this operation acts on.</p>"""
    tags: "aws_sdk_quicksight.types.column_tag_list.ColumnTagList"
    """<p>The dataset column tag, currently only used for geospatial type tagging.</p> <note> <p>This is not tags for the Amazon Web Services tagging feature.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagColumnOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    import aws_sdk_quicksight.types.column_tag_list

    out["Tags"] = aws_sdk_quicksight.types.column_tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagColumnOperation:
    out: TagColumnOperation = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("TagColumnOperation.column_name required")
    if "Tags" in data:
        import aws_sdk_quicksight.types.column_tag_list

        out["tags"] = aws_sdk_quicksight.types.column_tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagColumnOperation.tags required")
    return out
