"""Generated from Smithy shape ``com.amazonaws.fsx#CopyBackupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.kms_key_id
    import aws_sdk_fsx.types.region
    import aws_sdk_fsx.types.source_backup_id
    import aws_sdk_fsx.types.tags


class CopyBackupRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    source_backup_id: NotRequired["aws_sdk_fsx.types.source_backup_id.SourceBackupId"]
    """<p>The ID of the source backup. Specifies the ID of the backup that's being copied.</p>"""
    source_region: NotRequired["aws_sdk_fsx.types.region.Region"]
    """<p>The source Amazon Web Services Region of the backup. Specifies the Amazon Web Services Region from which the backup is being copied. The source and destination Regions must be in the same Amazon Web Services partition. If you don't specify a Region, <code>SourceRegion</code> defaults to the Region where the request is sent from (in-Region copy).</p>"""
    kms_key_id: NotRequired["aws_sdk_fsx.types.kms_key_id.KmsKeyId"]
    copy_tags: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A Boolean flag indicating whether tags from the source backup should be copied to the backup copy. This value defaults to <code>false</code>.</p> <p>If you set <code>CopyTags</code> to <code>true</code> and the source backup has existing tags, you can use the <code>Tags</code> parameter to create new tags, provided that the sum of the source backup tags and the new tags doesn't exceed 50. Both sets of tags are merged. If there are tag conflicts (for example, two tags with the same key but different values), the tags created with the <code>Tags</code> parameter take precedence.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyBackupRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "source_backup_id" in value:
        out["SourceBackupId"] = value["source_backup_id"]
    if "source_region" in value:
        out["SourceRegion"] = value["source_region"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "copy_tags" in value:
        out["CopyTags"] = value["copy_tags"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyBackupRequest:
    out: CopyBackupRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "SourceBackupId" in data:
        out["source_backup_id"] = data["SourceBackupId"]
    if "SourceRegion" in data:
        out["source_region"] = data["SourceRegion"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "CopyTags" in data:
        out["copy_tags"] = data["CopyTags"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
