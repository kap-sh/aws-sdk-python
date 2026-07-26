"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SourceDataSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.iso8601_date_time
    import capo_database_migration_service.types.string


class SourceDataSetting(TypedDict, closed=True):
    cdc_start_position: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The change data capture (CDC) start position for the source data provider.</p>"""
    cdc_start_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The change data capture (CDC) start time for the source data provider.</p>"""
    cdc_stop_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The change data capture (CDC) stop time for the source data provider.</p>"""
    slot_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the replication slot on the source data provider. This attribute is only valid for a PostgreSQL or Aurora PostgreSQL source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDataSetting) -> dict:
    out: dict = {}
    if "cdc_start_position" in value:
        out["CDCStartPosition"] = value["cdc_start_position"]
    if "cdc_start_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["CDCStartTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["cdc_start_time"]
            )
        )
    if "cdc_stop_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["CDCStopTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["cdc_stop_time"]
            )
        )
    if "slot_name" in value:
        out["SlotName"] = value["slot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceDataSetting:
    out: SourceDataSetting = {}  # type: ignore[typeddict-item]
    if "CDCStartPosition" in data:
        out["cdc_start_position"] = data["CDCStartPosition"]
    if "CDCStartTime" in data:
        import capo_database_migration_service.types.iso8601_date_time

        out["cdc_start_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["CDCStartTime"]
            )
        )
    if "CDCStopTime" in data:
        import capo_database_migration_service.types.iso8601_date_time

        out["cdc_stop_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["CDCStopTime"]
            )
        )
    if "SlotName" in data:
        out["slot_name"] = data["SlotName"]
    return out
