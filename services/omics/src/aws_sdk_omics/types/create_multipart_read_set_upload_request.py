"""Generated from Smithy shape ``com.amazonaws.omics#CreateMultipartReadSetUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.client_token
    import aws_sdk_omics.types.file_type
    import aws_sdk_omics.types.generated_from
    import aws_sdk_omics.types.read_set_description
    import aws_sdk_omics.types.read_set_name
    import aws_sdk_omics.types.reference_arn
    import aws_sdk_omics.types.sample_id
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.subject_id
    import aws_sdk_omics.types.tag_map


class CreateMultipartReadSetUploadRequest(TypedDict, closed=True):
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The sequence store ID for the store that is the destination of the multipart uploads.</p>"""
    client_token: NotRequired["aws_sdk_omics.types.client_token.ClientToken"]
    """<p>An idempotency token that can be used to avoid triggering multiple multipart uploads.</p>"""
    source_file_type: "aws_sdk_omics.types.file_type.FileType"
    """<p>The type of file being uploaded.</p>"""
    subject_id: "aws_sdk_omics.types.subject_id.SubjectId"
    """<p>The source's subject ID.</p>"""
    sample_id: "aws_sdk_omics.types.sample_id.SampleId"
    """<p>The source's sample ID.</p>"""
    generated_from: NotRequired["aws_sdk_omics.types.generated_from.GeneratedFrom"]
    """<p>Where the source originated.</p>"""
    reference_arn: NotRequired["aws_sdk_omics.types.reference_arn.ReferenceArn"]
    """<p>The ARN of the reference.</p>"""
    name: "aws_sdk_omics.types.read_set_name.ReadSetName"
    """<p>The name of the read set.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.read_set_description.ReadSetDescription"
    ]
    """<p>The description of the read set.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Any tags to add to the read set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultipartReadSetUploadRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["sourceFileType"] = value["source_file_type"]
    out["subjectId"] = value["subject_id"]
    out["sampleId"] = value["sample_id"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMultipartReadSetUploadRequest:
    out: CreateMultipartReadSetUploadRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "sourceFileType" in data:
        out["source_file_type"] = data["sourceFileType"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadRequest.source_file_type required"
        )
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadRequest.subject_id required"
        )
    if "sampleId" in data:
        out["sample_id"] = data["sampleId"]
    else:
        raise DeserializationError(
            "CreateMultipartReadSetUploadRequest.sample_id required"
        )
    if "generatedFrom" in data:
        out["generated_from"] = data["generatedFrom"]
    if "referenceArn" in data:
        out["reference_arn"] = data["referenceArn"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMultipartReadSetUploadRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    return out
