"""Generated from Smithy shape ``com.amazonaws.fsx#CreateBackupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.file_system_id
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.volume_id


class CreateBackupRequest(TypedDict):
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    """<p>The ID of the file system to back up.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    """<p>(Optional) A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    """<p>(Optional) The tags to apply to the backup at backup creation. The key value of the <code>Name</code> tag appears in the console as the backup name. If you have set <code>CopyTagsToBackups</code> to <code>true</code>, and you specify one or more tags using the <code>CreateBackup</code> operation, no existing file system tags are copied from the file system to the backup.</p>"""
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>(Optional) The ID of the FSx for ONTAP volume to back up.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBackupRequest) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBackupRequest:
    out: CreateBackupRequest = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    return out
