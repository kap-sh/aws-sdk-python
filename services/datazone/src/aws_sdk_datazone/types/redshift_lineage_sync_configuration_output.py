"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftLineageSyncConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_sync_schedule


class RedshiftLineageSyncConfigurationOutput(TypedDict):
    lineage_job_id: NotRequired["str"]
    """<p>The lineage job ID of the Amaon Redshift lineage sync configuration.</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether the Amaon Redshift lineage sync configuration is enabled.</p>"""
    schedule: NotRequired[
        "aws_sdk_datazone.types.lineage_sync_schedule.LineageSyncSchedule"
    ]
    """<p>The schedule of teh Amaon Redshift lineage sync configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftLineageSyncConfigurationOutput) -> dict:
    out: dict = {}
    if "lineage_job_id" in value:
        out["lineageJobId"] = value["lineage_job_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "schedule" in value:
        import aws_sdk_datazone.types.lineage_sync_schedule

        out["schedule"] = aws_sdk_datazone.types.lineage_sync_schedule.serialize_json(
            value["schedule"]
        )
    return out


def deserialize_json(data: dict) -> RedshiftLineageSyncConfigurationOutput:
    out: RedshiftLineageSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "lineageJobId" in data:
        out["lineage_job_id"] = data["lineageJobId"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "schedule" in data:
        import aws_sdk_datazone.types.lineage_sync_schedule

        out["schedule"] = aws_sdk_datazone.types.lineage_sync_schedule.deserialize_json(
            data["schedule"]
        )
    return out
