"""Generated from Smithy shape ``com.amazonaws.athena#ColumnInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.boolean
    import aws_sdk_athena.types.column_nullable
    import aws_sdk_athena.types.integer
    import aws_sdk_athena.types.string


class ColumnInfo(TypedDict):
    catalog_name: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>The catalog to which the query results belong.</p>"""
    schema_name: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>The schema name (database name) to which the query results belong.</p>"""
    table_name: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>The table name for the query results.</p>"""
    name: "aws_sdk_athena.types.string.String"
    """<p>The name of the column.</p>"""
    label: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>A column label.</p>"""
    type: "aws_sdk_athena.types.string.String"
    """<p>The data type of the column.</p>"""
    precision: "aws_sdk_athena.types.integer.Integer"
    """<p>For <code>DECIMAL</code> data types, specifies the total number of digits, up to 38. For performance reasons, we recommend up to 18 digits.</p>"""
    scale: "aws_sdk_athena.types.integer.Integer"
    """<p>For <code>DECIMAL</code> data types, specifies the total number of digits in the fractional part of the value. Defaults to 0.</p>"""
    nullable: NotRequired["aws_sdk_athena.types.column_nullable.ColumnNullable"]
    """<p>Unsupported constraint. This value always shows as <code>UNKNOWN</code>.</p>"""
    case_sensitive: "aws_sdk_athena.types.boolean.Boolean"
    """<p>Indicates whether values in the column are case-sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnInfo) -> dict:
    out: dict = {}
    if "catalog_name" in value:
        out["CatalogName"] = value["catalog_name"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    out["Name"] = value["name"]
    if "label" in value:
        out["Label"] = value["label"]
    out["Type"] = value["type"]
    out["Precision"] = value.get("precision", 0)
    out["Scale"] = value.get("scale", 0)
    if "nullable" in value:
        import aws_sdk_athena.types.column_nullable

        out["Nullable"] = aws_sdk_athena.types.column_nullable.serialize_aws_json_1_1(
            value["nullable"]
        )
    out["CaseSensitive"] = value.get("case_sensitive", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnInfo:
    out: ColumnInfo = {}  # type: ignore[typeddict-item]
    if "CatalogName" in data:
        out["catalog_name"] = data["CatalogName"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ColumnInfo.name required")
    if "Label" in data:
        out["label"] = data["Label"]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("ColumnInfo.type required")
    if "Precision" in data:
        out["precision"] = data["Precision"]
    else:
        out["precision"] = 0
    if "Scale" in data:
        out["scale"] = data["Scale"]
    else:
        out["scale"] = 0
    if "Nullable" in data:
        import aws_sdk_athena.types.column_nullable

        out["nullable"] = aws_sdk_athena.types.column_nullable.deserialize_aws_json_1_1(
            data["Nullable"]
        )
    if "CaseSensitive" in data:
        out["case_sensitive"] = data["CaseSensitive"]
    else:
        out["case_sensitive"] = False
    return out
