"""Generated from Smithy shape ``com.amazonaws.athena#Column``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.comment_string
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.type_string


class Column(TypedDict, closed=True):
    name: "aws_sdk_athena.types.name_string.NameString"
    """<p>The name of the column.</p>"""
    type: NotRequired["aws_sdk_athena.types.type_string.TypeString"]
    """<p>The data type of the column.</p>"""
    comment: NotRequired["aws_sdk_athena.types.comment_string.CommentString"]
    """<p>Optional information about the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Column) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Column:
    out: Column = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Column.name required")
    if "Type" in data:
        out["type"] = data["Type"]
    if "Comment" in data:
        out["comment"] = data["Comment"]
    return out
