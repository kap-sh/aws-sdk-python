"""Generated from Smithy shape ``com.amazonaws.omics#CreateMultipartReadSetUploadResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.file_type
    import aws_sdk_omics.types.generated_from
    import aws_sdk_omics.types.read_set_description
    import aws_sdk_omics.types.read_set_name
    import aws_sdk_omics.types.reference_arn
    import aws_sdk_omics.types.sample_id
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.subject_id
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.upload_id


class CreateMultipartReadSetUploadResponse(TypedDict):
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The sequence store ID for the store that the read set will be created in.</p>"""
    upload_id: "aws_sdk_omics.types.upload_id.UploadId"
    """<p>The ID for the initiated multipart upload.</p>"""
    source_file_type: "aws_sdk_omics.types.file_type.FileType"
    """<p>The file type of the read set source.</p>"""
    subject_id: "aws_sdk_omics.types.subject_id.SubjectId"
    """<p>The source's subject ID.</p>"""
    sample_id: "aws_sdk_omics.types.sample_id.SampleId"
    """<p>The source's sample ID.</p>"""
    generated_from: NotRequired["aws_sdk_omics.types.generated_from.GeneratedFrom"]
    """<p>The source of the read set.</p>"""
    reference_arn: "aws_sdk_omics.types.reference_arn.ReferenceArn"
    """<p>The read set source's reference ARN.</p>"""
    name: NotRequired["aws_sdk_omics.types.read_set_name.ReadSetName"]
    """<p>The name of the read set.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.read_set_description.ReadSetDescription"
    ]
    """<p>The description of the read set.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>The tags to add to the read set.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time of the multipart upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultipartReadSetUploadResponse) -> dict:
    out: dict = {}
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["uploadId"] = value["upload_id"]
    out["sourceFileType"] = value["source_file_type"]
    out["subjectId"] = value["subject_id"]
    out["sampleId"] = value["sample_id"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    out["referenceArn"] = value["reference_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateMultipartReadSetUploadResponse:
    out: CreateMultipartReadSetUploadResponse = {}  # type: ignore[typeddict-item]
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadResponse.sequence_store_id required"
        )
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadResponse.upload_id required"
        )
    if "sourceFileType" in data:
        out["source_file_type"] = data["sourceFileType"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadResponse.source_file_type required"
        )
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadResponse.subject_id required"
        )
    if "sampleId" in data:
        out["sample_id"] = data["sampleId"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadResponse.sample_id required"
        )
    if "generatedFrom" in data:
        out["generated_from"] = data["generatedFrom"]
    if "referenceArn" in data:
        out["reference_arn"] = data["referenceArn"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadResponse.reference_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadResponse.creation_time required"
        )
    return out
