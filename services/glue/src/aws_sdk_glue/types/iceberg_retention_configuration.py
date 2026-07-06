"""Generated from Smithy shape ``com.amazonaws.glue#IcebergRetentionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.nullable_integer


class IcebergRetentionConfiguration(TypedDict, closed=True):
    snapshot_retention_period_in_days: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of days to retain the Iceberg snapshots. If an input is not provided, the corresponding Iceberg table configuration field will be used or if not present, the default value 5 will be used.</p>"""
    number_of_snapshots_to_retain: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of Iceberg snapshots to retain within the retention period. If an input is not provided, the corresponding Iceberg table configuration field will be used or if not present, the default value 1 will be used.</p>"""
    clean_expired_files: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>If set to false, snapshots are only deleted from table metadata, and the underlying data and metadata files are not deleted.</p>"""
    run_rate_in_hours: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The interval in hours between retention job runs. This parameter controls how frequently the retention optimizer will run to clean up expired snapshots. The value must be between 3 and 168 hours (7 days). If an input is not provided, the default value 24 will be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergRetentionConfiguration) -> dict:
    out: dict = {}
    if "snapshot_retention_period_in_days" in value:
        out["snapshotRetentionPeriodInDays"] = value[
            "snapshot_retention_period_in_days"
        ]
    if "number_of_snapshots_to_retain" in value:
        out["numberOfSnapshotsToRetain"] = value["number_of_snapshots_to_retain"]
    if "clean_expired_files" in value:
        out["cleanExpiredFiles"] = value["clean_expired_files"]
    if "run_rate_in_hours" in value:
        out["runRateInHours"] = value["run_rate_in_hours"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergRetentionConfiguration:
    out: IcebergRetentionConfiguration = {}  # type: ignore[typeddict-item]
    if "snapshotRetentionPeriodInDays" in data:
        out["snapshot_retention_period_in_days"] = data["snapshotRetentionPeriodInDays"]
    if "numberOfSnapshotsToRetain" in data:
        out["number_of_snapshots_to_retain"] = data["numberOfSnapshotsToRetain"]
    if "cleanExpiredFiles" in data:
        out["clean_expired_files"] = data["cleanExpiredFiles"]
    if "runRateInHours" in data:
        out["run_rate_in_hours"] = data["runRateInHours"]
    return out
