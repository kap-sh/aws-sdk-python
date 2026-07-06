"""Generated from Smithy shape ``com.amazonaws.glue#Column``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_type_string
    import aws_sdk_glue.types.comment_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.parameters_map


class Column(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the <code>Column</code>.</p>"""
    type: NotRequired["aws_sdk_glue.types.column_type_string.ColumnTypeString"]
    """<p>The data type of the <code>Column</code>.</p>"""
    comment: NotRequired["aws_sdk_glue.types.comment_string.CommentString"]
    """<p>A free-form text comment.</p>"""
    parameters: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define properties associated with the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Column) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "parameters" in value:
        import aws_sdk_glue.types.parameters_map

        out["Parameters"] = aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
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
    if "Parameters" in data:
        import aws_sdk_glue.types.parameters_map

        out["parameters"] = aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
