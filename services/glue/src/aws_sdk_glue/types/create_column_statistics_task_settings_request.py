"""Generated from Smithy shape ``com.amazonaws.glue#CreateColumnStatisticsTaskSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_name_list
    import aws_sdk_glue.types.cron_expression
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.sample_size_percentage
    import aws_sdk_glue.types.tags_map


class CreateColumnStatisticsTaskSettingsRequest(TypedDict):
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table for which to generate column statistics.</p>"""
    role: "aws_sdk_glue.types.name_string.NameString"
    """<p>The role used for running the column statistics.</p>"""
    schedule: NotRequired["aws_sdk_glue.types.cron_expression.CronExpression"]
    """<p>A schedule for running the column statistics, specified in CRON syntax.</p>"""
    column_name_list: NotRequired["aws_sdk_glue.types.column_name_list.ColumnNameList"]
    """<p>A list of column names for which to run statistics.</p>"""
    sample_size: "aws_sdk_glue.types.sample_size_percentage.SampleSizePercentage"
    """<p>The percentage of data to sample.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The ID of the Data Catalog in which the database resides.</p>"""
    security_configuration: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Name of the security configuration that is used to encrypt CloudWatch logs.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>A map of tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateColumnStatisticsTaskSettingsRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["Role"] = value["role"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "column_name_list" in value:
        import aws_sdk_glue.types.column_name_list

        out["ColumnNameList"] = (
            aws_sdk_glue.types.column_name_list.serialize_aws_json_1_1(
                value["column_name_list"]
            )
        )
    out["SampleSize"] = value.get("sample_size", 0)
    if "catalog_id" in value:
        out["CatalogID"] = value["catalog_id"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateColumnStatisticsTaskSettingsRequest:
    out: CreateColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "CreateColumnStatisticsTaskSettingsRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "CreateColumnStatisticsTaskSettingsRequest.table_name required"
        )
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError(
            "CreateColumnStatisticsTaskSettingsRequest.role required"
        )
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    if "ColumnNameList" in data:
        import aws_sdk_glue.types.column_name_list

        out["column_name_list"] = (
            aws_sdk_glue.types.column_name_list.deserialize_aws_json_1_1(
                data["ColumnNameList"]
            )
        )
    if "SampleSize" in data:
        out["sample_size"] = data["SampleSize"]
    else:
        out["sample_size"] = 0
    if "CatalogID" in data:
        out["catalog_id"] = data["CatalogID"]
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
