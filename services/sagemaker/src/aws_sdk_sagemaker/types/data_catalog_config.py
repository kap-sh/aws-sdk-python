"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataCatalogConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.catalog
    import aws_sdk_sagemaker.types.database
    import aws_sdk_sagemaker.types.table_name


class DataCatalogConfig(TypedDict):
    table_name: NotRequired["aws_sdk_sagemaker.types.table_name.TableName"]
    """<p>The name of the Glue table.</p>"""
    catalog: NotRequired["aws_sdk_sagemaker.types.catalog.Catalog"]
    """<p>The name of the Glue table catalog.</p>"""
    database: NotRequired["aws_sdk_sagemaker.types.database.Database"]
    """<p>The name of the Glue table database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCatalogConfig) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "database" in value:
        out["Database"] = value["database"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataCatalogConfig:
    out: DataCatalogConfig = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    if "Database" in data:
        out["database"] = data["Database"]
    return out
