"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataMigrationStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer
    import capo_database_migration_service.types.iso8601_date_time
    import capo_database_migration_service.types.long


class DataMigrationStatistics(TypedDict, closed=True):
    tables_loaded: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of tables loaded in the current data migration run.</p>"""
    elapsed_time_millis: "capo_database_migration_service.types.long.Long"
    """<p>The elapsed duration of the data migration run.</p>"""
    tables_loading: "capo_database_migration_service.types.integer.Integer"
    """<p>The data migration's table loading progress.</p>"""
    full_load_percentage: "capo_database_migration_service.types.integer.Integer"
    """<p>The data migration's progress in the full-load migration phase.</p>"""
    cdc_latency: "capo_database_migration_service.types.integer.Integer"
    """<p>The current latency of the change data capture (CDC) operation.</p>"""
    tables_queued: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of tables that are waiting for processing.</p>"""
    tables_errored: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of tables that DMS failed to process.</p>"""
    start_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The time when the migration started.</p>"""
    stop_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The time when the migration stopped or failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataMigrationStatistics) -> dict:
    out: dict = {}
    out["TablesLoaded"] = value.get("tables_loaded", 0)
    out["ElapsedTimeMillis"] = value.get("elapsed_time_millis", 0)
    out["TablesLoading"] = value.get("tables_loading", 0)
    out["FullLoadPercentage"] = value.get("full_load_percentage", 0)
    out["CDCLatency"] = value.get("cdc_latency", 0)
    out["TablesQueued"] = value.get("tables_queued", 0)
    out["TablesErrored"] = value.get("tables_errored", 0)
    if "start_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["StartTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "stop_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["StopTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["stop_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataMigrationStatistics:
    out: DataMigrationStatistics = {}  # type: ignore[typeddict-item]
    if "TablesLoaded" in data:
        out["tables_loaded"] = data["TablesLoaded"]
    else:
        out["tables_loaded"] = 0
    if "ElapsedTimeMillis" in data:
        out["elapsed_time_millis"] = data["ElapsedTimeMillis"]
    else:
        out["elapsed_time_millis"] = 0
    if "TablesLoading" in data:
        out["tables_loading"] = data["TablesLoading"]
    else:
        out["tables_loading"] = 0
    if "FullLoadPercentage" in data:
        out["full_load_percentage"] = data["FullLoadPercentage"]
    else:
        out["full_load_percentage"] = 0
    if "CDCLatency" in data:
        out["cdc_latency"] = data["CDCLatency"]
    else:
        out["cdc_latency"] = 0
    if "TablesQueued" in data:
        out["tables_queued"] = data["TablesQueued"]
    else:
        out["tables_queued"] = 0
    if "TablesErrored" in data:
        out["tables_errored"] = data["TablesErrored"]
    else:
        out["tables_errored"] = 0
    if "StartTime" in data:
        import capo_database_migration_service.types.iso8601_date_time

        out["start_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "StopTime" in data:
        import capo_database_migration_service.types.iso8601_date_time

        out["stop_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["StopTime"]
            )
        )
    return out
