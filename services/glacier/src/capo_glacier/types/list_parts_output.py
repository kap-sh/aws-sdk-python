"""Generated from Smithy shape ``com.amazonaws.glacier#ListPartsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.long
    import capo_glacier.types.part_list
    import capo_glacier.types.string


class ListPartsOutput(TypedDict, closed=True):
    multipart_upload_id: NotRequired["capo_glacier.types.string.string"]
    """<p>The ID of the upload to which the parts are associated.</p>"""
    vault_arn: NotRequired["capo_glacier.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.</p>"""
    archive_description: NotRequired["capo_glacier.types.string.string"]
    """<p>The description of the archive that was specified in the Initiate Multipart Upload request.</p>"""
    part_size_in_bytes: "capo_glacier.types.long.long"
    """<p>The part size in bytes. This is the same value that you specified in the Initiate Multipart Upload request.</p>"""
    creation_date: NotRequired["capo_glacier.types.string.string"]
    """<p>The UTC time at which the multipart upload was initiated.</p>"""
    parts: NotRequired["capo_glacier.types.part_list.PartList"]
    """<p>A list of the part sizes of the multipart upload. Each object in the array contains a <code>RangeBytes</code> and <code>sha256-tree-hash</code> name/value pair.</p>"""
    marker: NotRequired["capo_glacier.types.string.string"]
    """<p>An opaque string that represents where to continue pagination of the results. You use the marker in a new List Parts request to obtain more jobs in the list. If there are no more parts, this value is <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPartsOutput) -> dict:
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
    if "parts" in value:
        import capo_glacier.types.part_list

        out["Parts"] = capo_glacier.types.part_list.serialize_json(value["parts"])
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> ListPartsOutput:
    out: ListPartsOutput = {}  # type: ignore[typeddict-item]
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
    if "Parts" in data:
        import capo_glacier.types.part_list

        out["parts"] = capo_glacier.types.part_list.deserialize_json(data["Parts"])
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
