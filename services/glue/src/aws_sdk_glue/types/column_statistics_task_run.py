"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsTaskRun``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.account_id
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.column_name_list
    import aws_sdk_glue.types.column_statistics_state
    import aws_sdk_glue.types.computation_type
    import aws_sdk_glue.types.crawler_security_configuration
    import aws_sdk_glue.types.database_name
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.non_negative_double
    import aws_sdk_glue.types.positive_integer
    import aws_sdk_glue.types.role
    import aws_sdk_glue.types.sample_size_percentage
    import aws_sdk_glue.types.table_name
    import aws_sdk_glue.types.timestamp


class ColumnStatisticsTaskRun(TypedDict):
    customer_id: NotRequired["aws_sdk_glue.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    column_statistics_task_run_id: NotRequired[
        "aws_sdk_glue.types.hash_string.HashString"
    ]
    """<p>The identifier for the particular column statistics task run.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.database_name.DatabaseName"]
    """<p>The database where the table resides.</p>"""
    table_name: NotRequired["aws_sdk_glue.types.table_name.TableName"]
    """<p>The name of the table for which column statistics is generated.</p>"""
    column_name_list: NotRequired["aws_sdk_glue.types.column_name_list.ColumnNameList"]
    """<p>A list of the column names. If none is supplied, all column names for the table will be used by default.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    role: NotRequired["aws_sdk_glue.types.role.Role"]
    """<p>The IAM role that the service assumes to generate statistics.</p>"""
    sample_size: "aws_sdk_glue.types.sample_size_percentage.SampleSizePercentage"
    """<p>The percentage of rows used to generate statistics. If none is supplied, the entire table will be used to generate stats.</p>"""
    security_configuration: NotRequired[
        "aws_sdk_glue.types.crawler_security_configuration.CrawlerSecurityConfiguration"
    ]
    """<p>Name of the security configuration that is used to encrypt CloudWatch logs for the column stats task run.</p>"""
    number_of_workers: "aws_sdk_glue.types.positive_integer.PositiveInteger"
    """<p>The number of workers used to generate column statistics. The job is preconfigured to autoscale up to 25 instances.</p>"""
    worker_type: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The type of workers being used for generating stats. The default is <code>g.1x</code>.</p>"""
    computation_type: NotRequired["aws_sdk_glue.types.computation_type.ComputationType"]
    """<p>The type of column statistics computation.</p>"""
    status: NotRequired[
        "aws_sdk_glue.types.column_statistics_state.ColumnStatisticsState"
    ]
    """<p>The status of the task run.</p>"""
    creation_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that this task was created.</p>"""
    last_updated: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The last point in time when this task was modified.</p>"""
    start_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The start time of the task.</p>"""
    end_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The end time of the task.</p>"""
    error_message: NotRequired[
        "aws_sdk_glue.types.description_string.DescriptionString"
    ]
    """<p>The error message for the job.</p>"""
    dpu_seconds: "aws_sdk_glue.types.non_negative_double.NonNegativeDouble"
    """<p>The calculated DPU usage in seconds for all autoscaled workers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsTaskRun) -> dict:
    out: dict = {}
    if "customer_id" in value:
        out["CustomerId"] = value["customer_id"]
    if "column_statistics_task_run_id" in value:
        out["ColumnStatisticsTaskRunId"] = value["column_statistics_task_run_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "column_name_list" in value:
        import aws_sdk_glue.types.column_name_list

        out["ColumnNameList"] = (
            aws_sdk_glue.types.column_name_list.serialize_aws_json_1_1(
                value["column_name_list"]
            )
        )
    if "catalog_id" in value:
        out["CatalogID"] = value["catalog_id"]
    if "role" in value:
        out["Role"] = value["role"]
    out["SampleSize"] = value.get("sample_size", 0)
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    out["NumberOfWorkers"] = value.get("number_of_workers", 0)
    if "worker_type" in value:
        out["WorkerType"] = value["worker_type"]
    if "computation_type" in value:
        import aws_sdk_glue.types.computation_type

        out["ComputationType"] = (
            aws_sdk_glue.types.computation_type.serialize_aws_json_1_1(
                value["computation_type"]
            )
        )
    if "status" in value:
        import aws_sdk_glue.types.column_statistics_state

        out["Status"] = (
            aws_sdk_glue.types.column_statistics_state.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_glue.types.timestamp

        out["CreationTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated" in value:
        import aws_sdk_glue.types.timestamp

        out["LastUpdated"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    if "start_time" in value:
        import aws_sdk_glue.types.timestamp

        out["StartTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_glue.types.timestamp

        out["EndTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    out["DPUSeconds"] = value.get("dpu_seconds", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnStatisticsTaskRun:
    out: ColumnStatisticsTaskRun = {}  # type: ignore[typeddict-item]
    if "CustomerId" in data:
        out["customer_id"] = data["CustomerId"]
    if "ColumnStatisticsTaskRunId" in data:
        out["column_statistics_task_run_id"] = data["ColumnStatisticsTaskRunId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "ColumnNameList" in data:
        import aws_sdk_glue.types.column_name_list

        out["column_name_list"] = (
            aws_sdk_glue.types.column_name_list.deserialize_aws_json_1_1(
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
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    else:
        out["number_of_workers"] = 0
    if "WorkerType" in data:
        out["worker_type"] = data["WorkerType"]
    if "ComputationType" in data:
        import aws_sdk_glue.types.computation_type

        out["computation_type"] = (
            aws_sdk_glue.types.computation_type.deserialize_aws_json_1_1(
                data["ComputationType"]
            )
        )
    if "Status" in data:
        import aws_sdk_glue.types.column_statistics_state

        out["status"] = (
            aws_sdk_glue.types.column_statistics_state.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_glue.types.timestamp

        out["creation_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastUpdated" in data:
        import aws_sdk_glue.types.timestamp

        out["last_updated"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if "StartTime" in data:
        import aws_sdk_glue.types.timestamp

        out["start_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_glue.types.timestamp

        out["end_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "DPUSeconds" in data:
        out["dpu_seconds"] = data["DPUSeconds"]
    else:
        out["dpu_seconds"] = 0
    return out
