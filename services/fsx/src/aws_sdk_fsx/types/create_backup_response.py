"""Generated from Smithy shape ``com.amazonaws.fsx#CreateBackupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.backup


class CreateBackupResponse(TypedDict, closed=True):
    backup: NotRequired["aws_sdk_fsx.types.backup.Backup"]
    """<p>A description of the backup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBackupResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import aws_sdk_fsx.types.backup

        out["Backup"] = aws_sdk_fsx.types.backup.serialize_aws_json_1_1(value["backup"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBackupResponse:
    out: CreateBackupResponse = {}  # type: ignore[typeddict-item]
    if "Backup" in data:
        import aws_sdk_fsx.types.backup

        out["backup"] = aws_sdk_fsx.types.backup.deserialize_aws_json_1_1(
            data["Backup"]
        )
    return out
