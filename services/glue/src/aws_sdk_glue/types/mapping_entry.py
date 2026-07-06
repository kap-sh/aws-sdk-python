"""Generated from Smithy shape ``com.amazonaws.glue#MappingEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.field_type
    import aws_sdk_glue.types.schema_path_string
    import aws_sdk_glue.types.table_name


class MappingEntry(TypedDict, closed=True):
    source_table: NotRequired["aws_sdk_glue.types.table_name.TableName"]
    """<p>The name of the source table.</p>"""
    source_path: NotRequired["aws_sdk_glue.types.schema_path_string.SchemaPathString"]
    """<p>The source path.</p>"""
    source_type: NotRequired["aws_sdk_glue.types.field_type.FieldType"]
    """<p>The source type.</p>"""
    target_table: NotRequired["aws_sdk_glue.types.table_name.TableName"]
    """<p>The target table.</p>"""
    target_path: NotRequired["aws_sdk_glue.types.schema_path_string.SchemaPathString"]
    """<p>The target path.</p>"""
    target_type: NotRequired["aws_sdk_glue.types.field_type.FieldType"]
    """<p>The target type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingEntry) -> dict:
    out: dict = {}
    if "source_table" in value:
        out["SourceTable"] = value["source_table"]
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "target_table" in value:
        out["TargetTable"] = value["target_table"]
    if "target_path" in value:
        out["TargetPath"] = value["target_path"]
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MappingEntry:
    out: MappingEntry = {}  # type: ignore[typeddict-item]
    if "SourceTable" in data:
        out["source_table"] = data["SourceTable"]
    if "SourcePath" in data:
        out["source_path"] = data["SourcePath"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "TargetTable" in data:
        out["target_table"] = data["TargetTable"]
    if "TargetPath" in data:
        out["target_path"] = data["TargetPath"]
    if "TargetType" in data:
        out["target_type"] = data["TargetType"]
    return out
