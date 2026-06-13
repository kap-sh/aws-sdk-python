"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.max_scheduled_runs_preview
    import aws_sdk_backup.types.string


class GetBackupPlanInput(TypedDict):
    backup_plan_id: "aws_sdk_backup.types.string.string"
    """<p>Uniquely identifies a backup plan.</p>"""
    version_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.</p>"""
    max_scheduled_runs_preview: (
        "aws_sdk_backup.types.max_scheduled_runs_preview.MaxScheduledRunsPreview"
    )
    """<p>Number of future scheduled backup runs to preview. When set to 0 (default), no scheduled runs preview is included in the response. Valid range is 0-10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackupPlanInput:
    out: GetBackupPlanInput = {}  # type: ignore[typeddict-item]
    return out
