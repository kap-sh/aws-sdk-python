"""Generated from Smithy shape ``com.amazonaws.backup#Lifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.boolean
    import capo_backup.types.lifecycle_delete_after_event
    import capo_backup.types.long


class Lifecycle(TypedDict, closed=True):
    move_to_cold_storage_after_days: NotRequired["capo_backup.types.long.Long"]
    """<p>The number of days after creation that a recovery point is moved to cold storage.</p>"""
    delete_after_days: NotRequired["capo_backup.types.long.Long"]
    """<p>The number of days after creation that a recovery point is deleted. This value must be at least 90 days after the number of days specified in <code>MoveToColdStorageAfterDays</code>.</p>"""
    opt_in_to_archive_for_supported_resources: NotRequired[
        "capo_backup.types.boolean.Boolean"
    ]
    """<p>If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.</p>"""
    delete_after_event: NotRequired[
        "capo_backup.types.lifecycle_delete_after_event.LifecycleDeleteAfterEvent"
    ]
    """<p>The event after which a recovery point is deleted. A recovery point with both <code>DeleteAfterDays</code> and <code>DeleteAfterEvent</code> will delete after whichever condition is satisfied first. Not valid as an input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Lifecycle) -> dict:
    out: dict = {}
    if "move_to_cold_storage_after_days" in value:
        out["MoveToColdStorageAfterDays"] = value["move_to_cold_storage_after_days"]
    if "delete_after_days" in value:
        out["DeleteAfterDays"] = value["delete_after_days"]
    if "opt_in_to_archive_for_supported_resources" in value:
        out["OptInToArchiveForSupportedResources"] = value[
            "opt_in_to_archive_for_supported_resources"
        ]
    if "delete_after_event" in value:
        import capo_backup.types.lifecycle_delete_after_event

        out["DeleteAfterEvent"] = (
            capo_backup.types.lifecycle_delete_after_event.serialize_json(
                value["delete_after_event"]
            )
        )
    return out


def deserialize_json(data: dict) -> Lifecycle:
    out: Lifecycle = {}  # type: ignore[typeddict-item]
    if "MoveToColdStorageAfterDays" in data:
        out["move_to_cold_storage_after_days"] = data["MoveToColdStorageAfterDays"]
    if "DeleteAfterDays" in data:
        out["delete_after_days"] = data["DeleteAfterDays"]
    if "OptInToArchiveForSupportedResources" in data:
        out["opt_in_to_archive_for_supported_resources"] = data[
            "OptInToArchiveForSupportedResources"
        ]
    if "DeleteAfterEvent" in data:
        import capo_backup.types.lifecycle_delete_after_event

        out["delete_after_event"] = (
            capo_backup.types.lifecycle_delete_after_event.deserialize_json(
                data["DeleteAfterEvent"]
            )
        )
    return out
