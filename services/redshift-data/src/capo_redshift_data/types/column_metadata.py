"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ColumnMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_data.types.bool
    import capo_redshift_data.types.integer
    import capo_redshift_data.types.string


class ColumnMetadata(TypedDict, closed=True):
    is_case_sensitive: "capo_redshift_data.types.bool.bool"
    """<p>A value that indicates whether the column is case-sensitive. </p>"""
    is_currency: "capo_redshift_data.types.bool.bool"
    """<p>A value that indicates whether the column contains currency values.</p>"""
    is_signed: "capo_redshift_data.types.bool.bool"
    """<p>A value that indicates whether an integer column is signed.</p>"""
    label: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The label for the column. </p>"""
    name: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The name of the column. </p>"""
    nullable: "capo_redshift_data.types.integer.Integer"
    """<p>A value that indicates whether the column is nullable. </p>"""
    precision: "capo_redshift_data.types.integer.Integer"
    """<p>The precision value of a decimal number column, or the column length for a non-numeric column. </p>"""
    scale: "capo_redshift_data.types.integer.Integer"
    """<p>The scale value of a decimal number column. </p>"""
    schema_name: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The name of the schema that contains the table that includes the column.</p>"""
    table_name: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The name of the table that includes the column. </p>"""
    type_name: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The database-specific data type of the column. </p>"""
    length: "capo_redshift_data.types.integer.Integer"
    """<p>The length of the column.</p>"""
    column_default: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The default value of the column. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnMetadata) -> dict:
    out: dict = {}
    out["isCaseSensitive"] = value.get("is_case_sensitive", False)
    out["isCurrency"] = value.get("is_currency", False)
    out["isSigned"] = value.get("is_signed", False)
    if "label" in value:
        out["label"] = value["label"]
    if "name" in value:
        out["name"] = value["name"]
    out["nullable"] = value.get("nullable", 0)
    out["precision"] = value.get("precision", 0)
    out["scale"] = value.get("scale", 0)
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    if "table_name" in value:
        out["tableName"] = value["table_name"]
    if "type_name" in value:
        out["typeName"] = value["type_name"]
    out["length"] = value.get("length", 0)
    if "column_default" in value:
        out["columnDefault"] = value["column_default"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnMetadata:
    out: ColumnMetadata = {}  # type: ignore[typeddict-item]
    if "isCaseSensitive" in data:
        out["is_case_sensitive"] = data["isCaseSensitive"]
    else:
        out["is_case_sensitive"] = False
    if "isCurrency" in data:
        out["is_currency"] = data["isCurrency"]
    else:
        out["is_currency"] = False
    if "isSigned" in data:
        out["is_signed"] = data["isSigned"]
    else:
        out["is_signed"] = False
    if "label" in data:
        out["label"] = data["label"]
    if "name" in data:
        out["name"] = data["name"]
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
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    if "length" in data:
        out["length"] = data["length"]
    else:
        out["length"] = 0
    if "columnDefault" in data:
        out["column_default"] = data["columnDefault"]
    return out
