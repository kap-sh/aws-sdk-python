"""Generated from Smithy shape ``com.amazonaws.omics#ImportReadSetSourceItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.file_type
    import aws_sdk_omics.types.generated_from
    import aws_sdk_omics.types.job_status_message
    import aws_sdk_omics.types.read_set_description
    import aws_sdk_omics.types.read_set_id
    import aws_sdk_omics.types.read_set_import_job_item_status
    import aws_sdk_omics.types.read_set_name
    import aws_sdk_omics.types.reference_arn
    import aws_sdk_omics.types.sample_id
    import aws_sdk_omics.types.source_files
    import aws_sdk_omics.types.subject_id
    import aws_sdk_omics.types.tag_map


class ImportReadSetSourceItem(TypedDict):
    source_files: "aws_sdk_omics.types.source_files.SourceFiles"
    """<p>The source files' location in Amazon S3.</p>"""
    source_file_type: "aws_sdk_omics.types.file_type.FileType"
    """<p>The source's file type.</p>"""
    status: (
        "aws_sdk_omics.types.read_set_import_job_item_status.ReadSetImportJobItemStatus"
    )
    """<p>The source's status.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.job_status_message.JobStatusMessage"
    ]
    """<p>The source's status message.</p>"""
    subject_id: "aws_sdk_omics.types.subject_id.SubjectId"
    """<p>The source's subject ID.</p>"""
    sample_id: "aws_sdk_omics.types.sample_id.SampleId"
    """<p>The source's sample ID.</p>"""
    generated_from: NotRequired["aws_sdk_omics.types.generated_from.GeneratedFrom"]
    """<p>Where the source originated.</p>"""
    reference_arn: NotRequired["aws_sdk_omics.types.reference_arn.ReferenceArn"]
    """<p>The source's genome reference ARN.</p>"""
    name: NotRequired["aws_sdk_omics.types.read_set_name.ReadSetName"]
    """<p>The source's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.read_set_description.ReadSetDescription"
    ]
    """<p>The source's description.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>The source's tags.</p>"""
    read_set_id: NotRequired["aws_sdk_omics.types.read_set_id.ReadSetId"]
    """<p>The source's read set ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportReadSetSourceItem) -> dict:
    out: dict = {}
    import aws_sdk_omics.types.source_files

    out["sourceFiles"] = aws_sdk_omics.types.source_files.serialize_json(
        value["source_files"]
    )
    out["sourceFileType"] = value["source_file_type"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    out["subjectId"] = value["subject_id"]
    out["sampleId"] = value["sample_id"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "read_set_id" in value:
        out["readSetId"] = value["read_set_id"]
    return out


def deserialize_json(data: dict) -> ImportReadSetSourceItem:
    out: ImportReadSetSourceItem = {}  # type: ignore[typeddict-item]
    if "sourceFiles" in data:
        import aws_sdk_omics.types.source_files

        out["source_files"] = aws_sdk_omics.types.source_files.deserialize_json(
            data["sourceFiles"]
        )
    else:
        raise DeserializationError("ImportReadSetSourceItem.source_files required")
    if "sourceFileType" in data:
        out["source_file_type"] = data["sourceFileType"]
    else:
        raise DeserializationError("ImportReadSetSourceItem.source_file_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportReadSetSourceItem.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    else:
        raise DeserializationError("ImportReadSetSourceItem.subject_id required")
    if "sampleId" in data:
        out["sample_id"] = data["sampleId"]
    else:
        raise DeserializationError("ImportReadSetSourceItem.sample_id required")
    if "generatedFrom" in data:
        out["generated_from"] = data["generatedFrom"]
    if "referenceArn" in data:
        out["reference_arn"] = data["referenceArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "readSetId" in data:
        out["read_set_id"] = data["readSetId"]
    return out
