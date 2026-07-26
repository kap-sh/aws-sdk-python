"""Generated from Smithy shape ``com.amazonaws.backup#CalculatedLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.timestamp


class CalculatedLifecycle(TypedDict, closed=True):
    move_to_cold_storage_at: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>A timestamp that specifies when to transition a recovery point to cold storage.</p>"""
    delete_at: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>A timestamp that specifies when to delete a recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedLifecycle) -> dict:
    out: dict = {}
    if "move_to_cold_storage_at" in value:
        import capo_backup.types.timestamp

        out["MoveToColdStorageAt"] = capo_backup.types.timestamp.serialize_json(
            value["move_to_cold_storage_at"]
        )
    if "delete_at" in value:
        import capo_backup.types.timestamp

        out["DeleteAt"] = capo_backup.types.timestamp.serialize_json(value["delete_at"])
    return out


def deserialize_json(data: dict) -> CalculatedLifecycle:
    out: CalculatedLifecycle = {}  # type: ignore[typeddict-item]
    if "MoveToColdStorageAt" in data:
        import capo_backup.types.timestamp

        out["move_to_cold_storage_at"] = capo_backup.types.timestamp.deserialize_json(
            data["MoveToColdStorageAt"]
        )
    if "DeleteAt" in data:
        import capo_backup.types.timestamp

        out["delete_at"] = capo_backup.types.timestamp.deserialize_json(
            data["DeleteAt"]
        )
    return out
