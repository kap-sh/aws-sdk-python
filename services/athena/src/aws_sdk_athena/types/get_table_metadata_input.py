"""Generated from Smithy shape ``com.amazonaws.athena#GetTableMetadataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.catalog_name_string
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.work_group_name


class GetTableMetadataInput(TypedDict):
    catalog_name: "aws_sdk_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog that contains the database and table metadata to return.</p>"""
    database_name: "aws_sdk_athena.types.name_string.NameString"
    """<p>The name of the database that contains the table metadata to return.</p>"""
    table_name: "aws_sdk_athena.types.name_string.NameString"
    """<p>The name of the table for which metadata is returned.</p>"""
    work_group: NotRequired["aws_sdk_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled Glue Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableMetadataInput) -> dict:
    out: dict = {}
    out["CatalogName"] = value["catalog_name"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableMetadataInput:
    out: GetTableMetadataInput = {}  # type: ignore[typeddict-item]
    if "CatalogName" in data:
        out["catalog_name"] = data["CatalogName"]
    else:
        raise DeserializationError("GetTableMetadataInput.catalog_name required")
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetTableMetadataInput.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetTableMetadataInput.table_name required")
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    return out
