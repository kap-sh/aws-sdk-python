"""Generated from Smithy shape ``com.amazonaws.backupsearch#BackupCreationTimeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime


class BackupCreationTimeFilter(TypedDict):
    created_after: NotRequired["datetime.datetime"]
    """<p>This timestamp includes recovery points only created after the specified time.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>This timestamp includes recovery points only created before the specified time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupCreationTimeFilter) -> dict:
    out: dict = {}
    if "created_after" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CreatedAfter"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["created_after"]
            )
        )
    if "created_before" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CreatedBefore"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["created_before"]
            )
        )
    return out


def deserialize_json(data: dict) -> BackupCreationTimeFilter:
    out: BackupCreationTimeFilter = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["created_after"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["created_before"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreatedBefore"]
            )
        )
    return out
