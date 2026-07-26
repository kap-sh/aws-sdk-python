"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsTaskSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.column_name_list
    import capo_glue.types.crawler_security_configuration
    import capo_glue.types.database_name
    import capo_glue.types.execution_attempt
    import capo_glue.types.role
    import capo_glue.types.sample_size_percentage
    import capo_glue.types.schedule
    import capo_glue.types.schedule_type
    import capo_glue.types.setting_source
    import capo_glue.types.table_name


class ColumnStatisticsTaskSettings(TypedDict, closed=True):
    database_name: NotRequired["capo_glue.types.database_name.DatabaseName"]
    """<p>The name of the database where the table resides.</p>"""
    table_name: NotRequired["capo_glue.types.table_name.TableName"]
    """<p>The name of the table for which to generate column statistics.</p>"""
    schedule: NotRequired["capo_glue.types.schedule.Schedule"]
    """<p>A schedule for running the column statistics, specified in CRON syntax.</p>"""
    column_name_list: NotRequired["capo_glue.types.column_name_list.ColumnNameList"]
    """<p>A list of column names for which to run statistics.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the database resides.</p>"""
    role: NotRequired["capo_glue.types.role.Role"]
    """<p>The role used for running the column statistics.</p>"""
    sample_size: "capo_glue.types.sample_size_percentage.SampleSizePercentage"
    """<p>The percentage of data to sample.</p>"""
    security_configuration: NotRequired[
        "capo_glue.types.crawler_security_configuration.CrawlerSecurityConfiguration"
    ]
    """<p>Name of the security configuration that is used to encrypt CloudWatch logs.</p>"""
    schedule_type: NotRequired["capo_glue.types.schedule_type.ScheduleType"]
    """<p>The type of schedule for a column statistics task. Possible values may be <code>CRON</code> or <code>AUTO</code>.</p>"""
    setting_source: NotRequired["capo_glue.types.setting_source.SettingSource"]
    """<p>The source of setting the column statistics task. Possible values may be <code>CATALOG</code> or <code>TABLE</code>.</p>"""
    last_execution_attempt: NotRequired[
        "capo_glue.types.execution_attempt.ExecutionAttempt"
    ]
    """<p>The last <code>ExecutionAttempt</code> for the column statistics task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsTaskSettings) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "schedule" in value:
        import capo_glue.types.schedule

        out["Schedule"] = capo_glue.types.schedule.serialize_aws_json_1_1(
            value["schedule"]
        )
    if "column_name_list" in value:
        import capo_glue.types.column_name_list

        out["ColumnNameList"] = capo_glue.types.column_name_list.serialize_aws_json_1_1(
            value["column_name_list"]
        )
    if "catalog_id" in value:
        out["CatalogID"] = value["catalog_id"]
    if "role" in value:
        out["Role"] = value["role"]
    out["SampleSize"] = value.get("sample_size", 0)
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "schedule_type" in value:
        import capo_glue.types.schedule_type

        out["ScheduleType"] = capo_glue.types.schedule_type.serialize_aws_json_1_1(
            value["schedule_type"]
        )
    if "setting_source" in value:
        import capo_glue.types.setting_source

        out["SettingSource"] = capo_glue.types.setting_source.serialize_aws_json_1_1(
            value["setting_source"]
        )
    if "last_execution_attempt" in value:
        import capo_glue.types.execution_attempt

        out["LastExecutionAttempt"] = (
            capo_glue.types.execution_attempt.serialize_aws_json_1_1(
                value["last_execution_attempt"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnStatisticsTaskSettings:
    out: ColumnStatisticsTaskSettings = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Schedule" in data:
        import capo_glue.types.schedule

        out["schedule"] = capo_glue.types.schedule.deserialize_aws_json_1_1(
            data["Schedule"]
        )
    if "ColumnNameList" in data:
        import capo_glue.types.column_name_list

        out["column_name_list"] = (
            capo_glue.types.column_name_list.deserialize_aws_json_1_1(
                data["ColumnNameList"]
            )
        )
    if "CatalogID" in data:
        out["catalog_id"] = data["CatalogID"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "SampleSize" in data:
        out["sample_size"] = data["SampleSize"]
    else:
        out["sample_size"] = 0
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    if "ScheduleType" in data:
        import capo_glue.types.schedule_type

        out["schedule_type"] = capo_glue.types.schedule_type.deserialize_aws_json_1_1(
            data["ScheduleType"]
        )
    if "SettingSource" in data:
        import capo_glue.types.setting_source

        out["setting_source"] = capo_glue.types.setting_source.deserialize_aws_json_1_1(
            data["SettingSource"]
        )
    if "LastExecutionAttempt" in data:
        import capo_glue.types.execution_attempt

        out["last_execution_attempt"] = (
            capo_glue.types.execution_attempt.deserialize_aws_json_1_1(
                data["LastExecutionAttempt"]
            )
        )
    return out
