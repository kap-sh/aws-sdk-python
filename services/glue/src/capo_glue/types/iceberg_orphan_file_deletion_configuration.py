"""Generated from Smithy shape ``com.amazonaws.glue#IcebergOrphanFileDeletionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.message_string
    import capo_glue.types.nullable_integer


class IcebergOrphanFileDeletionConfiguration(TypedDict, closed=True):
    orphan_file_retention_period_in_days: NotRequired[
        "capo_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of days that orphan files should be retained before file deletion. If an input is not provided, the default value 3 will be used.</p>"""
    location: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>Specifies a directory in which to look for files (defaults to the table's location). You may choose a sub-directory rather than the top-level table location.</p>"""
    run_rate_in_hours: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The interval in hours between orphan file deletion job runs. This parameter controls how frequently the orphan file deletion optimizer will run to clean up orphan files. The value must be between 3 and 168 hours (7 days). If an input is not provided, the default value 24 will be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergOrphanFileDeletionConfiguration) -> dict:
    out: dict = {}
    if "orphan_file_retention_period_in_days" in value:
        out["orphanFileRetentionPeriodInDays"] = value[
            "orphan_file_retention_period_in_days"
        ]
    if "location" in value:
        out["location"] = value["location"]
    if "run_rate_in_hours" in value:
        out["runRateInHours"] = value["run_rate_in_hours"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergOrphanFileDeletionConfiguration:
    out: IcebergOrphanFileDeletionConfiguration = {}  # type: ignore[typeddict-item]
    if "orphanFileRetentionPeriodInDays" in data:
        out["orphan_file_retention_period_in_days"] = data[
            "orphanFileRetentionPeriodInDays"
        ]
    if "location" in data:
        out["location"] = data["location"]
    if "runRateInHours" in data:
        out["run_rate_in_hours"] = data["runRateInHours"]
    return out
