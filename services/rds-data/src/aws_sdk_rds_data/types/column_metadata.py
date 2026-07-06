"""Generated from Smithy shape ``com.amazonaws.rdsdata#ColumnMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.boolean
    import aws_sdk_rds_data.types.integer
    import aws_sdk_rds_data.types.string


class ColumnMetadata(TypedDict, closed=True):
    name: NotRequired["aws_sdk_rds_data.types.string.String"]
    """<p>The name of the column.</p>"""
    type: "aws_sdk_rds_data.types.integer.Integer"
    """<p>The type of the column.</p>"""
    type_name: NotRequired["aws_sdk_rds_data.types.string.String"]
    """<p>The database-specific data type of the column.</p>"""
    label: NotRequired["aws_sdk_rds_data.types.string.String"]
    """<p>The label for the column.</p>"""
    schema_name: NotRequired["aws_sdk_rds_data.types.string.String"]
    """<p>The name of the schema that owns the table that includes the column.</p>"""
    table_name: NotRequired["aws_sdk_rds_data.types.string.String"]
    """<p>The name of the table that includes the column.</p>"""
    is_auto_increment: "aws_sdk_rds_data.types.boolean.Boolean"
    """<p>A value that indicates whether the column increments automatically.</p>"""
    is_signed: "aws_sdk_rds_data.types.boolean.Boolean"
    """<p>A value that indicates whether an integer column is signed.</p>"""
    is_currency: "aws_sdk_rds_data.types.boolean.Boolean"
    """<p>A value that indicates whether the column contains currency values.</p>"""
    is_case_sensitive: "aws_sdk_rds_data.types.boolean.Boolean"
    """<p>A value that indicates whether the column is case-sensitive.</p>"""
    nullable: "aws_sdk_rds_data.types.integer.Integer"
    """<p>A value that indicates whether the column is nullable.</p>"""
    precision: "aws_sdk_rds_data.types.integer.Integer"
    """<p>The precision value of a decimal number column.</p>"""
    scale: "aws_sdk_rds_data.types.integer.Integer"
    """<p>The scale value of a decimal number column.</p>"""
    array_base_column_type: "aws_sdk_rds_data.types.integer.Integer"
    """<p>The type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["type"] = value.get("type", 0)
    if "type_name" in value:
        out["typeName"] = value["type_name"]
    if "label" in value:
        out["label"] = value["label"]
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    if "table_name" in value:
        out["tableName"] = value["table_name"]
    out["isAutoIncrement"] = value.get("is_auto_increment", False)
    out["isSigned"] = value.get("is_signed", False)
    out["isCurrency"] = value.get("is_currency", False)
    out["isCaseSensitive"] = value.get("is_case_sensitive", False)
    out["nullable"] = value.get("nullable", 0)
    out["precision"] = value.get("precision", 0)
    out["scale"] = value.get("scale", 0)
    out["arrayBaseColumnType"] = value.get("array_base_column_type", 0)
    return out


def deserialize_json(data: dict) -> ColumnMetadata:
    out: ColumnMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    else:
        out["type"] = 0
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    if "label" in data:
        out["label"] = data["label"]
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    if "isAutoIncrement" in data:
        out["is_auto_increment"] = data["isAutoIncrement"]
    else:
        out["is_auto_increment"] = False
    if "isSigned" in data:
        out["is_signed"] = data["isSigned"]
    else:
        out["is_signed"] = False
    if "isCurrency" in data:
        out["is_currency"] = data["isCurrency"]
    else:
        out["is_currency"] = False
    if "isCaseSensitive" in data:
        out["is_case_sensitive"] = data["isCaseSensitive"]
    else:
        out["is_case_sensitive"] = False
    if "nullable" in data:
        out["nullable"] = data["nullable"]
    else:
        out["nullable"] = 0
    if "precision" in data:
        out["precision"] = data["precision"]
    else:
        out["precision"] = 0
    if "scale" in data:
        out["scale"] = data["scale"]
    else:
        out["scale"] = 0
    if "arrayBaseColumnType" in data:
        out["array_base_column_type"] = data["arrayBaseColumnType"]
    else:
        out["array_base_column_type"] = 0
    return out
