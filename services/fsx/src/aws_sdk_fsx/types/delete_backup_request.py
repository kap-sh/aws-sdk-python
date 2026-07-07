"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteBackupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.backup_id
    import aws_sdk_fsx.types.client_request_token


class DeleteBackupRequest(TypedDict, closed=True):
    backup_id: NotRequired["aws_sdk_fsx.types.backup_id.BackupId"]
    """<p>The ID of the backup that you want to delete.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    """<p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This parameter is automatically filled on your behalf when using the CLI or SDK.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBackupRequest) -> dict:
    out: dict = {}
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBackupRequest:
    out: DeleteBackupRequest = {}  # type: ignore[typeddict-item]
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
