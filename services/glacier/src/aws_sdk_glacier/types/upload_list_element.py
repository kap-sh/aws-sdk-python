"""Generated from Smithy shape ``com.amazonaws.glacier#UploadListElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.long
    import aws_sdk_glacier.types.string


class UploadListElement(TypedDict):
    multipart_upload_id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The ID of a multipart upload.</p>"""
    vault_arn: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the vault that contains the archive.</p>"""
    archive_description: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The description of the archive that was specified in the Initiate Multipart Upload request.</p>"""
    part_size_in_bytes: "aws_sdk_glacier.types.long.long"
    """<p>The part size, in bytes, specified in the Initiate Multipart Upload request. This is the size of all the parts in the upload except the last part, which may be smaller than this size.</p>"""
    creation_date: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The UTC time at which the multipart upload was initiated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadListElement) -> dict:
    out: dict = {}
    if "multipart_upload_id" in value:
        out["MultipartUploadId"] = value["multipart_upload_id"]
    if "vault_arn" in value:
        out["VaultARN"] = value["vault_arn"]
    if "archive_description" in value:
        out["ArchiveDescription"] = value["archive_description"]
    out["PartSizeInBytes"] = value.get("part_size_in_bytes", 0)
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    return out


def deserialize_json(data: dict) -> UploadListElement:
    out: UploadListElement = {}  # type: ignore[typeddict-item]
    if "MultipartUploadId" in data:
        out["multipart_upload_id"] = data["MultipartUploadId"]
    if "VaultARN" in data:
        out["vault_arn"] = data["VaultARN"]
    if "ArchiveDescription" in data:
        out["archive_description"] = data["ArchiveDescription"]
    if "PartSizeInBytes" in data:
        out["part_size_in_bytes"] = data["PartSizeInBytes"]
    else:
        out["part_size_in_bytes"] = 0
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    return out
