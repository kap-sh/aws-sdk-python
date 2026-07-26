"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftLineageSyncConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.lineage_sync_schedule


class RedshiftLineageSyncConfigurationInput(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Specifies whether the Amaon Redshift lineage sync configuration is enabled.</p>"""
    schedule: NotRequired[
        "capo_datazone.types.lineage_sync_schedule.LineageSyncSchedule"
    ]
    """<p>The schedule of the Amaon Redshift lineage sync configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftLineageSyncConfigurationInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "schedule" in value:
        import capo_datazone.types.lineage_sync_schedule

        out["schedule"] = capo_datazone.types.lineage_sync_schedule.serialize_json(
            value["schedule"]
        )
    return out


def deserialize_json(data: dict) -> RedshiftLineageSyncConfigurationInput:
    out: RedshiftLineageSyncConfigurationInput = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "schedule" in data:
        import capo_datazone.types.lineage_sync_schedule

        out["schedule"] = capo_datazone.types.lineage_sync_schedule.deserialize_json(
            data["schedule"]
        )
    return out
