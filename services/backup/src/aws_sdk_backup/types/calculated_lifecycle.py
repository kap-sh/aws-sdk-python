"""Generated from Smithy shape ``com.amazonaws.backup#CalculatedLifecycle``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_backup.types.timestamp

class CalculatedLifecycle(TypedDict):
    move_to_cold_storage_at: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>A timestamp that specifies when to transition a recovery point to cold storage.</p>"""
    delete_at: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>A timestamp that specifies when to delete a recovery point.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CalculatedLifecycle) -> dict:
    out: dict = {}
    if "move_to_cold_storage_at" in value:
        import aws_sdk_backup.types.timestamp
        out["MoveToColdStorageAt"] = aws_sdk_backup.types.timestamp.serialize_json(value["move_to_cold_storage_at"])
    if "delete_at" in value:
        import aws_sdk_backup.types.timestamp
        out["DeleteAt"] = aws_sdk_backup.types.timestamp.serialize_json(value["delete_at"])
    return out


def deserialize_json(data: dict) -> CalculatedLifecycle:
    out: CalculatedLifecycle = {}  # type: ignore[typeddict-item]
    if "MoveToColdStorageAt" in data:
        import aws_sdk_backup.types.timestamp
        out["move_to_cold_storage_at"] = aws_sdk_backup.types.timestamp.deserialize_json(data["MoveToColdStorageAt"])
    if "DeleteAt" in data:
        import aws_sdk_backup.types.timestamp
        out["delete_at"] = aws_sdk_backup.types.timestamp.deserialize_json(data["DeleteAt"])
    return out