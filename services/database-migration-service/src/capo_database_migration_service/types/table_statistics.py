"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TableStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.double_optional
    import capo_database_migration_service.types.long
    import capo_database_migration_service.types.long_optional
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class TableStatistics(TypedDict, closed=True):
    schema_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The schema name.</p>"""
    table_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the table.</p>"""
    inserts: "capo_database_migration_service.types.long.Long"
    """<p>The number of insert actions performed on a table.</p>"""
    deletes: "capo_database_migration_service.types.long.Long"
    """<p>The number of delete actions performed on a table.</p>"""
    updates: "capo_database_migration_service.types.long.Long"
    """<p>The number of update actions performed on a table.</p>"""
    ddls: "capo_database_migration_service.types.long.Long"
    """<p>The data definition language (DDL) used to build and modify the structure of your tables.</p>"""
    applied_inserts: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of insert actions applied on a target table.</p>"""
    applied_deletes: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of delete actions applied on a target table.</p>"""
    applied_updates: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of update actions applied on a target table.</p>"""
    applied_ddls: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of data definition language (DDL) statements used to build and modify the structure of your tables applied on the target.</p>"""
    full_load_rows: "capo_database_migration_service.types.long.Long"
    """<p>The number of rows added during the full load operation.</p>"""
    full_load_condtnl_chk_failed_rows: "capo_database_migration_service.types.long.Long"
    """<p>The number of rows that failed conditional checks during the full load operation (valid only for migrations where DynamoDB is the target).</p>"""
    full_load_error_rows: "capo_database_migration_service.types.long.Long"
    """<p>The number of rows that failed to load during the full load operation (valid only for migrations where DynamoDB is the target).</p>"""
    full_load_start_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time when the full load operation started.</p>"""
    full_load_end_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time when the full load operation completed.</p>"""
    full_load_reloaded: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates if the table was reloaded (<code>true</code>) or loaded as part of a new full load operation (<code>false</code>).</p>"""
    last_update_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The last time a table was updated.</p>"""
    table_state: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The state of the tables described.</p> <p>Valid states: Table does not exist | Before load | Full load | Table completed | Table cancelled | Table error | Table is being reloaded</p>"""
    validation_pending_records: "capo_database_migration_service.types.long.Long"
    """<p>The number of records that have yet to be validated.</p>"""
    validation_failed_records: "capo_database_migration_service.types.long.Long"
    """<p>The number of records that failed validation.</p>"""
    validation_suspended_records: "capo_database_migration_service.types.long.Long"
    """<p>The number of records that couldn't be validated.</p>"""
    validation_state: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The validation state of the table.</p> <p>This parameter can have the following values:</p> <ul> <li> <p>Not enabled – Validation isn't enabled for the table in the migration task.</p> </li> <li> <p>Pending records – Some records in the table are waiting for validation.</p> </li> <li> <p>Mismatched records – Some records in the table don't match between the source and target.</p> </li> <li> <p>Suspended records – Some records in the table couldn't be validated.</p> </li> <li> <p>No primary key –The table couldn't be validated because it has no primary key.</p> </li> <li> <p>Table error – The table wasn't validated because it's in an error state and some data wasn't migrated.</p> </li> <li> <p>Validated – All rows in the table are validated. If the table is updated, the status can change from Validated.</p> </li> <li> <p>Error – The table couldn't be validated because of an unexpected error.</p> </li> <li> <p>Pending validation – The table is waiting validation.</p> </li> <li> <p>Preparing table – Preparing the table enabled in the migration task for validation.</p> </li> <li> <p>Pending revalidation – All rows in the table are pending validation after the table was updated.</p> </li> </ul>"""
    validation_state_details: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Additional details about the state of validation.</p>"""
    resync_state: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Records the current state of table resynchronization in the migration task.</p> <p>This parameter can have the following values:</p> <ul> <li> <p>Not enabled – Resync is not enabled for the table in the migration task.</p> </li> <li> <p>Pending – The tables are waiting for resync.</p> </li> <li> <p>In progress – Resync in progress for some records in the table.</p> </li> <li> <p>No primary key – The table could not be resynced because it has no primary key.</p> </li> <li> <p>Last resync at: <code>date/time</code> – Resync session is finished at time. Time provided in UTC format.</p> </li> </ul>"""
    resync_rows_attempted: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>Records the total number of mismatched data rows where the system attempted to apply fixes in the target database.</p>"""
    resync_rows_succeeded: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>Records the total number of mismatched data rows where fixes were successfully applied in the target database.</p>"""
    resync_rows_failed: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>Records the total number of mismatched data rows where fix attempts failed in the target database.</p>"""
    resync_progress: NotRequired[
        "capo_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>Calculates the percentage of failed validations that were successfully resynced to the system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableStatistics) -> dict:
    out: dict = {}
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    out["Inserts"] = value.get("inserts", 0)
    out["Deletes"] = value.get("deletes", 0)
    out["Updates"] = value.get("updates", 0)
    out["Ddls"] = value.get("ddls", 0)
    if "applied_inserts" in value:
        out["AppliedInserts"] = value["applied_inserts"]
    if "applied_deletes" in value:
        out["AppliedDeletes"] = value["applied_deletes"]
    if "applied_updates" in value:
        out["AppliedUpdates"] = value["applied_updates"]
    if "applied_ddls" in value:
        out["AppliedDdls"] = value["applied_ddls"]
    out["FullLoadRows"] = value.get("full_load_rows", 0)
    out["FullLoadCondtnlChkFailedRows"] = value.get(
        "full_load_condtnl_chk_failed_rows", 0
    )
    out["FullLoadErrorRows"] = value.get("full_load_error_rows", 0)
    if "full_load_start_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["FullLoadStartTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["full_load_start_time"]
            )
        )
    if "full_load_end_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["FullLoadEndTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["full_load_end_time"]
            )
        )
    if "full_load_reloaded" in value:
        out["FullLoadReloaded"] = value["full_load_reloaded"]
    if "last_update_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["LastUpdateTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    if "table_state" in value:
        out["TableState"] = value["table_state"]
    out["ValidationPendingRecords"] = value.get("validation_pending_records", 0)
    out["ValidationFailedRecords"] = value.get("validation_failed_records", 0)
    out["ValidationSuspendedRecords"] = value.get("validation_suspended_records", 0)
    if "validation_state" in value:
        out["ValidationState"] = value["validation_state"]
    if "validation_state_details" in value:
        out["ValidationStateDetails"] = value["validation_state_details"]
    if "resync_state" in value:
        out["ResyncState"] = value["resync_state"]
    if "resync_rows_attempted" in value:
        out["ResyncRowsAttempted"] = value["resync_rows_attempted"]
    if "resync_rows_succeeded" in value:
        out["ResyncRowsSucceeded"] = value["resync_rows_succeeded"]
    if "resync_rows_failed" in value:
        out["ResyncRowsFailed"] = value["resync_rows_failed"]
    if "resync_progress" in value:
        out["ResyncProgress"] = value["resync_progress"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableStatistics:
    out: TableStatistics = {}  # type: ignore[typeddict-item]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Inserts" in data:
        out["inserts"] = data["Inserts"]
    else:
        out["inserts"] = 0
    if "Deletes" in data:
        out["deletes"] = data["Deletes"]
    else:
        out["deletes"] = 0
    if "Updates" in data:
        out["updates"] = data["Updates"]
    else:
        out["updates"] = 0
    if "Ddls" in data:
        out["ddls"] = data["Ddls"]
    else:
        out["ddls"] = 0
    if "AppliedInserts" in data:
        out["applied_inserts"] = data["AppliedInserts"]
    if "AppliedDeletes" in data:
        out["applied_deletes"] = data["AppliedDeletes"]
    if "AppliedUpdates" in data:
        out["applied_updates"] = data["AppliedUpdates"]
    if "AppliedDdls" in data:
        out["applied_ddls"] = data["AppliedDdls"]
    if "FullLoadRows" in data:
        out["full_load_rows"] = data["FullLoadRows"]
    else:
        out["full_load_rows"] = 0
    if "FullLoadCondtnlChkFailedRows" in data:
        out["full_load_condtnl_chk_failed_rows"] = data["FullLoadCondtnlChkFailedRows"]
    else:
        out["full_load_condtnl_chk_failed_rows"] = 0
    if "FullLoadErrorRows" in data:
        out["full_load_error_rows"] = data["FullLoadErrorRows"]
    else:
        out["full_load_error_rows"] = 0
    if "FullLoadStartTime" in data:
        import capo_database_migration_service.types.t_stamp

        out["full_load_start_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FullLoadStartTime"]
            )
        )
    if "FullLoadEndTime" in data:
        import capo_database_migration_service.types.t_stamp

        out["full_load_end_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FullLoadEndTime"]
            )
        )
    if "FullLoadReloaded" in data:
        out["full_load_reloaded"] = data["FullLoadReloaded"]
    if "LastUpdateTime" in data:
        import capo_database_migration_service.types.t_stamp

        out["last_update_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    if "TableState" in data:
        out["table_state"] = data["TableState"]
    if "ValidationPendingRecords" in data:
        out["validation_pending_records"] = data["ValidationPendingRecords"]
    else:
        out["validation_pending_records"] = 0
    if "ValidationFailedRecords" in data:
        out["validation_failed_records"] = data["ValidationFailedRecords"]
    else:
        out["validation_failed_records"] = 0
    if "ValidationSuspendedRecords" in data:
        out["validation_suspended_records"] = data["ValidationSuspendedRecords"]
    else:
        out["validation_suspended_records"] = 0
    if "ValidationState" in data:
        out["validation_state"] = data["ValidationState"]
    if "ValidationStateDetails" in data:
        out["validation_state_details"] = data["ValidationStateDetails"]
    if "ResyncState" in data:
        out["resync_state"] = data["ResyncState"]
    if "ResyncRowsAttempted" in data:
        out["resync_rows_attempted"] = data["ResyncRowsAttempted"]
    if "ResyncRowsSucceeded" in data:
        out["resync_rows_succeeded"] = data["ResyncRowsSucceeded"]
    if "ResyncRowsFailed" in data:
        out["resync_rows_failed"] = data["ResyncRowsFailed"]
    if "ResyncProgress" in data:
        out["resync_progress"] = data["ResyncProgress"]
    return out
