"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskRun``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.account_id
    import aws_sdk_glue.types.byte_count
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.database_name
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.materialized_view_refresh_state
    import aws_sdk_glue.types.materialized_view_refresh_type
    import aws_sdk_glue.types.non_negative_double
    import aws_sdk_glue.types.role
    import aws_sdk_glue.types.table_name
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.uui_dv4


class MaterializedViewRefreshTaskRun(TypedDict):
    customer_id: NotRequired["aws_sdk_glue.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    materialized_view_refresh_task_run_id: NotRequired[
        "aws_sdk_glue.types.uui_dv4.UUIDv4"
    ]
    """<p>The identifier of the materialized view refresh task run.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.database_name.DatabaseName"]
    """<p>The database where the table resides.</p>"""
    table_name: NotRequired["aws_sdk_glue.types.table_name.TableName"]
    """<p>The name of the table for which statistics is generated.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.</p>"""
    role: NotRequired["aws_sdk_glue.types.role.Role"]
    """<p>The IAM role that the service assumes to generate statistics.</p>"""
    status: NotRequired[
        "aws_sdk_glue.types.materialized_view_refresh_state.MaterializedViewRefreshState"
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
    refresh_type: NotRequired[
        "aws_sdk_glue.types.materialized_view_refresh_type.MaterializedViewRefreshType"
    ]
    """<p>The type of the refresh task run. Either FULL or INCREMENTAL.</p>"""
    processed_bytes: NotRequired["aws_sdk_glue.types.byte_count.ByteCount"]
    """<p>The number of bytes the refresh task run has scanned to refresh the materialized view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaterializedViewRefreshTaskRun) -> dict:
    out: dict = {}
    if "customer_id" in value:
        out["CustomerId"] = value["customer_id"]
    if "materialized_view_refresh_task_run_id" in value:
        out["MaterializedViewRefreshTaskRunId"] = value[
            "materialized_view_refresh_task_run_id"
        ]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "role" in value:
        out["Role"] = value["role"]
    if "status" in value:
        import aws_sdk_glue.types.materialized_view_refresh_state

        out["Status"] = (
            aws_sdk_glue.types.materialized_view_refresh_state.serialize_aws_json_1_1(
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
    if "refresh_type" in value:
        import aws_sdk_glue.types.materialized_view_refresh_type

        out["RefreshType"] = (
            aws_sdk_glue.types.materialized_view_refresh_type.serialize_aws_json_1_1(
                value["refresh_type"]
            )
        )
    if "processed_bytes" in value:
        out["ProcessedBytes"] = value["processed_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaterializedViewRefreshTaskRun:
    out: MaterializedViewRefreshTaskRun = {}  # type: ignore[typeddict-item]
    if "CustomerId" in data:
        out["customer_id"] = data["CustomerId"]
    if "MaterializedViewRefreshTaskRunId" in data:
        out["materialized_view_refresh_task_run_id"] = data[
            "MaterializedViewRefreshTaskRunId"
        ]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "Status" in data:
        import aws_sdk_glue.types.materialized_view_refresh_state

        out["status"] = (
            aws_sdk_glue.types.materialized_view_refresh_state.deserialize_aws_json_1_1(
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
    if "RefreshType" in data:
        import aws_sdk_glue.types.materialized_view_refresh_type

        out["refresh_type"] = (
            aws_sdk_glue.types.materialized_view_refresh_type.deserialize_aws_json_1_1(
                data["RefreshType"]
            )
        )
    if "ProcessedBytes" in data:
        out["processed_bytes"] = data["ProcessedBytes"]
    return out
