"""Generated from Smithy shape ``com.amazonaws.fsx#CopyBackupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.backup


class CopyBackupResponse(TypedDict, closed=True):
    backup: NotRequired["capo_fsx.types.backup.Backup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyBackupResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import capo_fsx.types.backup

        out["Backup"] = capo_fsx.types.backup.serialize_aws_json_1_1(value["backup"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyBackupResponse:
    out: CopyBackupResponse = {}  # type: ignore[typeddict-item]
    if "Backup" in data:
        import capo_fsx.types.backup

        out["backup"] = capo_fsx.types.backup.deserialize_aws_json_1_1(data["Backup"])
    return out
