"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.creation_job_id
    import aws_sdk_omics.types.creation_type
    import aws_sdk_omics.types.e_tag
    import aws_sdk_omics.types.file_type
    import aws_sdk_omics.types.read_set_arn
    import aws_sdk_omics.types.read_set_description
    import aws_sdk_omics.types.read_set_files
    import aws_sdk_omics.types.read_set_id
    import aws_sdk_omics.types.read_set_name
    import aws_sdk_omics.types.read_set_status
    import aws_sdk_omics.types.read_set_status_message
    import aws_sdk_omics.types.reference_arn
    import aws_sdk_omics.types.sample_id
    import aws_sdk_omics.types.sequence_information
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.subject_id


class GetReadSetMetadataResponse(TypedDict):
    id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The read set's ID.</p>"""
    arn: "aws_sdk_omics.types.read_set_arn.ReadSetArn"
    """<p>The read set's ARN.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    subject_id: NotRequired["aws_sdk_omics.types.subject_id.SubjectId"]
    """<p>The read set's subject ID.</p>"""
    sample_id: NotRequired["aws_sdk_omics.types.sample_id.SampleId"]
    """<p>The read set's sample ID.</p>"""
    status: "aws_sdk_omics.types.read_set_status.ReadSetStatus"
    """<p>The read set's status.</p>"""
    name: NotRequired["aws_sdk_omics.types.read_set_name.ReadSetName"]
    """<p>The read set's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.read_set_description.ReadSetDescription"
    ]
    """<p>The read set's description.</p>"""
    file_type: "aws_sdk_omics.types.file_type.FileType"
    """<p>The read set's file type.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the read set was created.</p>"""
    sequence_information: NotRequired[
        "aws_sdk_omics.types.sequence_information.SequenceInformation"
    ]
    """<p>The read set's sequence information.</p>"""
    reference_arn: NotRequired["aws_sdk_omics.types.reference_arn.ReferenceArn"]
    """<p>The read set's genome reference ARN.</p>"""
    files: NotRequired["aws_sdk_omics.types.read_set_files.ReadSetFiles"]
    """<p>The read set's files.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.read_set_status_message.ReadSetStatusMessage"
    ]
    """<p>The status message for a read set. It provides more detail as to why the read set has a status. </p>"""
    creation_type: NotRequired["aws_sdk_omics.types.creation_type.CreationType"]
    """<p> The creation type of the read set. </p>"""
    etag: NotRequired["aws_sdk_omics.types.e_tag.ETag"]
    """<p>The entity tag (ETag) is a hash of the object meant to represent its semantic content.</p>"""
    creation_job_id: NotRequired["aws_sdk_omics.types.creation_job_id.CreationJobId"]
    """<p>The read set's creation job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetMetadataResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    if "subject_id" in value:
        out["subjectId"] = value["subject_id"]
    if "sample_id" in value:
        out["sampleId"] = value["sample_id"]
    out["status"] = value["status"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["fileType"] = value["file_type"]
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "sequence_information" in value:
        import aws_sdk_omics.types.sequence_information

        out["sequenceInformation"] = (
            aws_sdk_omics.types.sequence_information.serialize_json(
                value["sequence_information"]
            )
        )
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    if "files" in value:
        import aws_sdk_omics.types.read_set_files

        out["files"] = aws_sdk_omics.types.read_set_files.serialize_json(value["files"])
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_type" in value:
        out["creationType"] = value["creation_type"]
    if "etag" in value:
        import aws_sdk_omics.types.e_tag

        out["etag"] = aws_sdk_omics.types.e_tag.serialize_json(value["etag"])
    if "creation_job_id" in value:
        out["creationJobId"] = value["creation_job_id"]
    return out


def deserialize_json(data: dict) -> GetReadSetMetadataResponse:
    out: GetReadSetMetadataResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetReadSetMetadataResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetReadSetMetadataResponse.arn required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "GetReadSetMetadataResponse.sequence_store_id required"
        )
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    if "sampleId" in data:
        out["sample_id"] = data["sampleId"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetReadSetMetadataResponse.status required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "fileType" in data:
        out["file_type"] = data["fileType"]
    else:
        raise DeserializationError("GetReadSetMetadataResponse.file_type required")
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetReadSetMetadataResponse.creation_time required")
    if "sequenceInformation" in data:
        import aws_sdk_omics.types.sequence_information

        out["sequence_information"] = (
            aws_sdk_omics.types.sequence_information.deserialize_json(
                data["sequenceInformation"]
            )
        )
    if "referenceArn" in data:
        out["reference_arn"] = data["referenceArn"]
    if "files" in data:
        import aws_sdk_omics.types.read_set_files

        out["files"] = aws_sdk_omics.types.read_set_files.deserialize_json(
            data["files"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationType" in data:
        out["creation_type"] = data["creationType"]
    if "etag" in data:
        import aws_sdk_omics.types.e_tag

        out["etag"] = aws_sdk_omics.types.e_tag.deserialize_json(data["etag"])
    if "creationJobId" in data:
        out["creation_job_id"] = data["creationJobId"]
    return out
