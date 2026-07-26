"""Generated from Smithy shape ``com.amazonaws.efs#BackupPolicyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.backup_policy


class BackupPolicyDescription(TypedDict, closed=True):
    backup_policy: NotRequired["capo_efs.types.backup_policy.BackupPolicy"]
    """<p>Describes the file system's backup policy, indicating whether automatic backups are turned on or off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupPolicyDescription) -> dict:
    out: dict = {}
    if "backup_policy" in value:
        import capo_efs.types.backup_policy

        out["BackupPolicy"] = capo_efs.types.backup_policy.serialize_json(
            value["backup_policy"]
        )
    return out


def deserialize_json(data: dict) -> BackupPolicyDescription:
    out: BackupPolicyDescription = {}  # type: ignore[typeddict-item]
    if "BackupPolicy" in data:
        import capo_efs.types.backup_policy

        out["backup_policy"] = capo_efs.types.backup_policy.deserialize_json(
            data["BackupPolicy"]
        )
    return out
