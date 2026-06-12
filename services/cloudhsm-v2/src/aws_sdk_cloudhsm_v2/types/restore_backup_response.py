"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#RestoreBackupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backup


class RestoreBackupResponse(TypedDict):
    backup: NotRequired["aws_sdk_cloudhsm_v2.types.backup.Backup"]
    """<p>Information on the <code>Backup</code> object created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreBackupResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import aws_sdk_cloudhsm_v2.types.backup

        out["Backup"] = aws_sdk_cloudhsm_v2.types.backup.serialize_aws_json_1_1(
            value["backup"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreBackupResponse:
    out: RestoreBackupResponse = {}  # type: ignore[typeddict-item]
    if "Backup" in data:
        import aws_sdk_cloudhsm_v2.types.backup

        out["backup"] = aws_sdk_cloudhsm_v2.types.backup.deserialize_aws_json_1_1(
            data["Backup"]
        )
    return out
