"""Generated from Smithy shape ``com.amazonaws.glue#StartColumnStatisticsTaskRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_name_list
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.sample_size_percentage


class StartColumnStatisticsTaskRunRequest(TypedDict):
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table to generate statistics.</p>"""
    column_name_list: NotRequired["aws_sdk_glue.types.column_name_list.ColumnNameList"]
    """<p>A list of the column names to generate statistics. If none is supplied, all column names for the table will be used by default.</p>"""
    role: "aws_sdk_glue.types.name_string.NameString"
    """<p>The IAM role that the service assumes to generate statistics.</p>"""
    sample_size: "aws_sdk_glue.types.sample_size_percentage.SampleSizePercentage"
    """<p>The percentage of rows used to generate statistics. If none is supplied, the entire table will be used to generate stats.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The ID of the Data Catalog where the table reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    security_configuration: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Name of the security configuration that is used to encrypt CloudWatch logs for the column stats task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartColumnStatisticsTaskRunRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "column_name_list" in value:
        import aws_sdk_glue.types.column_name_list

        out["ColumnNameList"] = (
            aws_sdk_glue.types.column_name_list.serialize_aws_json_1_1(
                value["column_name_list"]
            )
        )
    out["Role"] = value["role"]
    out["SampleSize"] = value.get("sample_size", 0)
    if "catalog_id" in value:
        out["CatalogID"] = value["catalog_id"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartColumnStatisticsTaskRunRequest:
    out: StartColumnStatisticsTaskRunRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "StartColumnStatisticsTaskRunRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "StartColumnStatisticsTaskRunRequest.table_name required"
        )
    if "ColumnNameList" in data:
        import aws_sdk_glue.types.column_name_list

        out["column_name_list"] = (
            aws_sdk_glue.types.column_name_list.deserialize_aws_json_1_1(
                data["ColumnNameList"]
            )
        )
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("StartColumnStatisticsTaskRunRequest.role required")
    if "SampleSize" in data:
        out["sample_size"] = data["SampleSize"]
    else:
        out["sample_size"] = 0
    if "CatalogID" in data:
        out["catalog_id"] = data["CatalogID"]
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    return out
