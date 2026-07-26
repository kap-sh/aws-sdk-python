"""Generated from Smithy shape ``com.amazonaws.backupsearch#BackupCreationTimeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class BackupCreationTimeFilter(TypedDict, closed=True):
    created_after: NotRequired["datetime.datetime"]
    """<p>This timestamp includes recovery points only created after the specified time.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>This timestamp includes recovery points only created before the specified time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupCreationTimeFilter) -> dict:
    out: dict = {}
    if "created_after" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["CreatedAfter"] = capo_backupsearch.types._prelude.timestamp.serialize_json(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["CreatedBefore"] = (
            capo_backupsearch.types._prelude.timestamp.serialize_json(
                value["created_before"]
            )
        )
    return out


def deserialize_json(data: dict) -> BackupCreationTimeFilter:
    out: BackupCreationTimeFilter = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import capo_backupsearch.types._prelude.timestamp

        out["created_after"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import capo_backupsearch.types._prelude.timestamp

        out["created_before"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreatedBefore"]
            )
        )
    return out
