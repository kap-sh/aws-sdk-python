"""Generated from Smithy shape ``com.amazonaws.omics#MultipartReadSetUploadListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.file_type
    import capo_omics.types.generated_from
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_name
    import capo_omics.types.reference_arn
    import capo_omics.types.sample_id
    import capo_omics.types.sequence_store_id
    import capo_omics.types.subject_id
    import capo_omics.types.tag_map
    import capo_omics.types.upload_id


class MultipartReadSetUploadListItem(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p> The sequence store ID used for the multipart upload. </p>"""
    upload_id: "capo_omics.types.upload_id.UploadId"
    """<p> The ID for the initiated multipart upload. </p>"""
    source_file_type: "capo_omics.types.file_type.FileType"
    """<p> The type of file the read set originated from. </p>"""
    subject_id: "capo_omics.types.subject_id.SubjectId"
    """<p> The read set source's subject ID. </p>"""
    sample_id: "capo_omics.types.sample_id.SampleId"
    """<p> The read set source's sample ID. </p>"""
    generated_from: "capo_omics.types.generated_from.GeneratedFrom"
    """<p> The source of an uploaded part. </p>"""
    reference_arn: "capo_omics.types.reference_arn.ReferenceArn"
    """<p> The source's reference ARN. </p>"""
    name: NotRequired["capo_omics.types.read_set_name.ReadSetName"]
    """<p> The name of a read set. </p>"""
    description: NotRequired["capo_omics.types.read_set_description.ReadSetDescription"]
    """<p> The description of a read set. </p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p> Any tags you wish to add to a read set. </p>"""
    creation_time: "datetime.datetime"
    """<p> The time stamp for when a direct upload was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultipartReadSetUploadListItem) -> dict:
    out: dict = {}
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["uploadId"] = value["upload_id"]
    out["sourceFileType"] = value["source_file_type"]
    out["subjectId"] = value["subject_id"]
    out["sampleId"] = value["sample_id"]
    out["generatedFrom"] = value["generated_from"]
    out["referenceArn"] = value["reference_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    import capo_omics.types._prelude.timestamp

    out["creationTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> MultipartReadSetUploadListItem:
    out: MultipartReadSetUploadListItem = {}  # type: ignore[typeddict-item]
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "MultipartReadSetUploadListItem.sequence_store_id required"
        )
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("MultipartReadSetUploadListItem.upload_id required")
    if "sourceFileType" in data:
        out["source_file_type"] = data["sourceFileType"]
    else:
        raise DeserializationError(
            "MultipartReadSetUploadListItem.source_file_type required"
        )
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    else:
        raise DeserializationError("MultipartReadSetUploadListItem.subject_id required")
    if "sampleId" in data:
        out["sample_id"] = data["sampleId"]
    else:
        raise DeserializationError("MultipartReadSetUploadListItem.sample_id required")
    if "generatedFrom" in data:
        out["generated_from"] = data["generatedFrom"]
    else:
        raise DeserializationError(
            "MultipartReadSetUploadListItem.generated_from required"
        )
    if "referenceArn" in data:
        out["reference_arn"] = data["referenceArn"]
    else:
        raise DeserializationError(
            "MultipartReadSetUploadListItem.reference_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if "creationTime" in data:
        import capo_omics.types._prelude.timestamp

        out["creation_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "MultipartReadSetUploadListItem.creation_time required"
        )
    return out
