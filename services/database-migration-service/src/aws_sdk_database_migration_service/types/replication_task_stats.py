"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskStats``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.integer
    import aws_sdk_database_migration_service.types.long
    import aws_sdk_database_migration_service.types.t_stamp


class ReplicationTaskStats(TypedDict):
    full_load_progress_percent: (
        "aws_sdk_database_migration_service.types.integer.Integer"
    )
    """<p>The percent complete for the full load migration task.</p>"""
    elapsed_time_millis: "aws_sdk_database_migration_service.types.long.Long"
    """<p>The elapsed time of the task, in milliseconds.</p>"""
    tables_loaded: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of tables loaded for this task.</p>"""
    tables_loading: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of tables currently loading for this task.</p>"""
    tables_queued: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of tables queued for this task.</p>"""
    tables_errored: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of errors that have occurred during this task.</p>"""
    fresh_start_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task was started either with a fresh start or a target reload.</p>"""
    start_date: NotRequired["aws_sdk_database_migration_service.types.t_stamp.TStamp"]
    r"""<p>The date the replication task was started either with a fresh start or a resume. For more information, see <a href=\"https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType\">StartReplicationTaskType</a>.</p>"""
    stop_date: NotRequired["aws_sdk_database_migration_service.types.t_stamp.TStamp"]
    """<p>The date the replication task was stopped.</p>"""
    full_load_start_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task full load was started.</p>"""
    full_load_finish_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task full load was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskStats) -> dict:
    out: dict = {}
    out["FullLoadProgressPercent"] = value.get("full_load_progress_percent", 0)
    out["ElapsedTimeMillis"] = value.get("elapsed_time_millis", 0)
    out["TablesLoaded"] = value.get("tables_loaded", 0)
    out["TablesLoading"] = value.get("tables_loading", 0)
    out["TablesQueued"] = value.get("tables_queued", 0)
    out["TablesErrored"] = value.get("tables_errored", 0)
    if "fresh_start_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["FreshStartDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["fresh_start_date"]
            )
        )
    if "start_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["StartDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["start_date"]
            )
        )
    if "stop_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["StopDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["stop_date"]
            )
        )
    if "full_load_start_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["FullLoadStartDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["full_load_start_date"]
            )
        )
    if "full_load_finish_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["FullLoadFinishDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["full_load_finish_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationTaskStats:
    out: ReplicationTaskStats = {}  # type: ignore[typeddict-item]
    if "FullLoadProgressPercent" in data:
        out["full_load_progress_percent"] = data["FullLoadProgressPercent"]
    else:
        out["full_load_progress_percent"] = 0
    if "ElapsedTimeMillis" in data:
        out["elapsed_time_millis"] = data["ElapsedTimeMillis"]
    else:
        out["elapsed_time_millis"] = 0
    if "TablesLoaded" in data:
        out["tables_loaded"] = data["TablesLoaded"]
    else:
        out["tables_loaded"] = 0
    if "TablesLoading" in data:
        out["tables_loading"] = data["TablesLoading"]
    else:
        out["tables_loading"] = 0
    if "TablesQueued" in data:
        out["tables_queued"] = data["TablesQueued"]
    else:
        out["tables_queued"] = 0
    if "TablesErrored" in data:
        out["tables_errored"] = data["TablesErrored"]
    else:
        out["tables_errored"] = 0
    if "FreshStartDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["fresh_start_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FreshStartDate"]
            )
        )
    if "StartDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["start_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["StartDate"]
            )
        )
    if "StopDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["stop_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["StopDate"]
            )
        )
    if "FullLoadStartDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["full_load_start_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FullLoadStartDate"]
            )
        )
    if "FullLoadFinishDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["full_load_finish_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FullLoadFinishDate"]
            )
        )
    return out
