"""Generated from Smithy shape ``com.amazonaws.omics#ImportReferenceSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.job_status_message
    import aws_sdk_omics.types.reference_description
    import aws_sdk_omics.types.reference_id
    import aws_sdk_omics.types.reference_import_job_item_status
    import aws_sdk_omics.types.reference_name
    import aws_sdk_omics.types.s3_uri
    import aws_sdk_omics.types.tag_map


class ImportReferenceSourceItem(TypedDict, closed=True):
    source_file: NotRequired["aws_sdk_omics.types.s3_uri.S3Uri"]
    """<p>The source file's location in Amazon S3.</p>"""
    status: "aws_sdk_omics.types.reference_import_job_item_status.ReferenceImportJobItemStatus"
    """<p>The source's status.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.job_status_message.JobStatusMessage"
    ]
    """<p>The source's status message.</p>"""
    name: NotRequired["aws_sdk_omics.types.reference_name.ReferenceName"]
    """<p>The source's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The source's description.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>The source's tags.</p>"""
    reference_id: NotRequired["aws_sdk_omics.types.reference_id.ReferenceId"]
    """<p>The source's reference ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportReferenceSourceItem) -> dict:
    out: dict = {}
    if "source_file" in value:
        out["sourceFile"] = value["source_file"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> ImportReferenceSourceItem:
    out: ImportReferenceSourceItem = {}  # type: ignore[typeddict-item]
    if "sourceFile" in data:
        out["source_file"] = data["sourceFile"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportReferenceSourceItem.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    return out
