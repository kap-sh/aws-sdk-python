"""Generated from Smithy shape ``com.amazonaws.databrew#DataCatalogInputDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.catalog_id
    import aws_sdk_databrew.types.database_name
    import aws_sdk_databrew.types.s3_location
    import aws_sdk_databrew.types.table_name


class DataCatalogInputDefinition(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_databrew.types.catalog_id.CatalogId"]
    """<p>The unique identifier of the Amazon Web Services account that holds the Data Catalog that stores the data.</p>"""
    database_name: "aws_sdk_databrew.types.database_name.DatabaseName"
    """<p>The name of a database in the Data Catalog.</p>"""
    table_name: "aws_sdk_databrew.types.table_name.TableName"
    """<p>The name of a database table in the Data Catalog. This table corresponds to a DataBrew dataset.</p>"""
    temp_directory: NotRequired["aws_sdk_databrew.types.s3_location.S3Location"]
    """<p>Represents an Amazon location where DataBrew can store intermediate results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataCatalogInputDefinition) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "temp_directory" in value:
        import aws_sdk_databrew.types.s3_location

        out["TempDirectory"] = aws_sdk_databrew.types.s3_location.serialize_json(
            value["temp_directory"]
        )
    return out


def deserialize_json(data: dict) -> DataCatalogInputDefinition:
    out: DataCatalogInputDefinition = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DataCatalogInputDefinition.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DataCatalogInputDefinition.table_name required")
    if "TempDirectory" in data:
        import aws_sdk_databrew.types.s3_location

        out["temp_directory"] = aws_sdk_databrew.types.s3_location.deserialize_json(
            data["TempDirectory"]
        )
    return out
