"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.creation_type
    import capo_omics.types.e_tag
    import capo_omics.types.file_type
    import capo_omics.types.read_set_arn
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_id
    import capo_omics.types.read_set_name
    import capo_omics.types.read_set_status
    import capo_omics.types.read_set_status_message
    import capo_omics.types.reference_arn
    import capo_omics.types.sample_id
    import capo_omics.types.sequence_information
    import capo_omics.types.sequence_store_id
    import capo_omics.types.subject_id


class ReadSetListItem(TypedDict, closed=True):
    id: "capo_omics.types.read_set_id.ReadSetId"
    """<p>The read set's ID.</p>"""
    arn: "capo_omics.types.read_set_arn.ReadSetArn"
    """<p>The read set's ARN.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    subject_id: NotRequired["capo_omics.types.subject_id.SubjectId"]
    """<p>The read set's subject ID.</p>"""
    sample_id: NotRequired["capo_omics.types.sample_id.SampleId"]
    """<p>The read set's sample ID.</p>"""
    status: "capo_omics.types.read_set_status.ReadSetStatus"
    """<p>The read set's status.</p>"""
    name: NotRequired["capo_omics.types.read_set_name.ReadSetName"]
    """<p>The read set's name.</p>"""
    description: NotRequired["capo_omics.types.read_set_description.ReadSetDescription"]
    """<p>The read set's description.</p>"""
    reference_arn: NotRequired["capo_omics.types.reference_arn.ReferenceArn"]
    """<p>The read set's genome reference ARN.</p>"""
    file_type: "capo_omics.types.file_type.FileType"
    """<p>The read set's file type.</p>"""
    sequence_information: NotRequired[
        "capo_omics.types.sequence_information.SequenceInformation"
    ]
    creation_time: "datetime.datetime"
    """<p>When the read set was created.</p>"""
    status_message: NotRequired[
        "capo_omics.types.read_set_status_message.ReadSetStatusMessage"
    ]
    """<p> The status for a read set. It provides more detail as to why the read set has a status. </p>"""
    creation_type: NotRequired["capo_omics.types.creation_type.CreationType"]
    """<p> The creation type of the read set. </p>"""
    etag: NotRequired["capo_omics.types.e_tag.ETag"]
    """<p>The entity tag (ETag) is a hash of the object representing its semantic content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetListItem) -> dict:
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
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    out["fileType"] = value["file_type"]
    if "sequence_information" in value:
        import capo_omics.types.sequence_information

        out["sequenceInformation"] = (
            capo_omics.types.sequence_information.serialize_json(
                value["sequence_information"]
            )
        )
    import capo_omics.types._prelude.timestamp

    out["creationTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_type" in value:
        out["creationType"] = value["creation_type"]
    if "etag" in value:
        import capo_omics.types.e_tag

        out["etag"] = capo_omics.types.e_tag.serialize_json(value["etag"])
    return out


def deserialize_json(data: dict) -> ReadSetListItem:
    out: ReadSetListItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ReadSetListItem.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ReadSetListItem.arn required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError("ReadSetListItem.sequence_store_id required")
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    if "sampleId" in data:
        out["sample_id"] = data["sampleId"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ReadSetListItem.status required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "referenceArn" in data:
        out["reference_arn"] = data["referenceArn"]
    if "fileType" in data:
        out["file_type"] = data["fileType"]
    else:
        raise DeserializationError("ReadSetListItem.file_type required")
    if "sequenceInformation" in data:
        import capo_omics.types.sequence_information

        out["sequence_information"] = (
            capo_omics.types.sequence_information.deserialize_json(
                data["sequenceInformation"]
            )
        )
    if "creationTime" in data:
        import capo_omics.types._prelude.timestamp

        out["creation_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ReadSetListItem.creation_time required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationType" in data:
        out["creation_type"] = data["creationType"]
    if "etag" in data:
        import capo_omics.types.e_tag

        out["etag"] = capo_omics.types.e_tag.deserialize_json(data["etag"])
    return out
