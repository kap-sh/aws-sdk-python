"""Generated from Smithy shape ``com.amazonaws.glue#GlueStudioSchemaColumn``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_type_string
    import aws_sdk_glue.types.glue_studio_column_name_string


class GlueStudioSchemaColumn(TypedDict):
    name: "aws_sdk_glue.types.glue_studio_column_name_string.GlueStudioColumnNameString"
    """<p>The name of the column in the Glue Studio schema.</p>"""
    type: NotRequired["aws_sdk_glue.types.column_type_string.ColumnTypeString"]
    """<p>The hive type for this column in the Glue Studio schema.</p>"""
    glue_studio_type: NotRequired[
        "aws_sdk_glue.types.column_type_string.ColumnTypeString"
    ]
    """<p>The data type of the column as defined in Glue Studio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueStudioSchemaColumn) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "glue_studio_type" in value:
        out["GlueStudioType"] = value["glue_studio_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GlueStudioSchemaColumn:
    out: GlueStudioSchemaColumn = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GlueStudioSchemaColumn.name required")
    if "Type" in data:
        out["type"] = data["Type"]
    if "GlueStudioType" in data:
        out["glue_studio_type"] = data["GlueStudioType"]
    return out
