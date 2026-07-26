"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.creation_job_id
    import capo_omics.types.md5
    import capo_omics.types.reference_arn
    import capo_omics.types.reference_creation_type
    import capo_omics.types.reference_description
    import capo_omics.types.reference_files
    import capo_omics.types.reference_id
    import capo_omics.types.reference_name
    import capo_omics.types.reference_status
    import capo_omics.types.reference_store_id


class GetReferenceMetadataResponse(TypedDict, closed=True):
    id: "capo_omics.types.reference_id.ReferenceId"
    """<p>The reference's ID.</p>"""
    arn: "capo_omics.types.reference_arn.ReferenceArn"
    """<p>The reference's ARN.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The reference's reference store ID.</p>"""
    md5: "capo_omics.types.md5.Md5"
    """<p>The reference's MD5 checksum.</p>"""
    status: NotRequired["capo_omics.types.reference_status.ReferenceStatus"]
    """<p>The reference's status.</p>"""
    name: NotRequired["capo_omics.types.reference_name.ReferenceName"]
    """<p>The reference's name.</p>"""
    description: NotRequired[
        "capo_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The reference's description.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the reference was created.</p>"""
    update_time: "datetime.datetime"
    """<p>When the reference was updated.</p>"""
    files: NotRequired["capo_omics.types.reference_files.ReferenceFiles"]
    """<p>The reference's files.</p>"""
    creation_type: NotRequired[
        "capo_omics.types.reference_creation_type.ReferenceCreationType"
    ]
    """<p>The reference's creation type.</p>"""
    creation_job_id: NotRequired["capo_omics.types.creation_job_id.CreationJobId"]
    """<p>The reference's creation job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceMetadataResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["md5"] = value["md5"]
    if "status" in value:
        out["status"] = value["status"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_omics.types._prelude.timestamp

    out["creationTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_omics.types._prelude.timestamp

    out["updateTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    if "files" in value:
        import capo_omics.types.reference_files

        out["files"] = capo_omics.types.reference_files.serialize_json(value["files"])
    if "creation_type" in value:
        out["creationType"] = value["creation_type"]
    if "creation_job_id" in value:
        out["creationJobId"] = value["creation_job_id"]
    return out


def deserialize_json(data: dict) -> GetReferenceMetadataResponse:
    out: GetReferenceMetadataResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetReferenceMetadataResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetReferenceMetadataResponse.arn required")
    if "referenceStoreId" in data:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        raise DeserializationError(
            "GetReferenceMetadataResponse.reference_store_id required"
        )
    if "md5" in data:
        out["md5"] = data["md5"]
    else:
        raise DeserializationError("GetReferenceMetadataResponse.md5 required")
    if "status" in data:
        out["status"] = data["status"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationTime" in data:
        import capo_omics.types._prelude.timestamp

        out["creation_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetReferenceMetadataResponse.creation_time required"
        )
    if "updateTime" in data:
        import capo_omics.types._prelude.timestamp

        out["update_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("GetReferenceMetadataResponse.update_time required")
    if "files" in data:
        import capo_omics.types.reference_files

        out["files"] = capo_omics.types.reference_files.deserialize_json(data["files"])
    if "creationType" in data:
        out["creation_type"] = data["creationType"]
    if "creationJobId" in data:
        out["creation_job_id"] = data["creationJobId"]
    return out
