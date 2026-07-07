"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.creation_type
    import aws_sdk_omics.types.generated_from
    import aws_sdk_omics.types.read_set_name
    import aws_sdk_omics.types.read_set_status
    import aws_sdk_omics.types.reference_arn_filter
    import aws_sdk_omics.types.sample_id
    import aws_sdk_omics.types.subject_id


class ReadSetFilter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_omics.types.read_set_name.ReadSetName"]
    """<p>A name to filter on.</p>"""
    status: NotRequired["aws_sdk_omics.types.read_set_status.ReadSetStatus"]
    """<p>A status to filter on.</p>"""
    reference_arn: NotRequired[
        "aws_sdk_omics.types.reference_arn_filter.ReferenceArnFilter"
    ]
    """<p>A genome reference ARN to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""
    sample_id: NotRequired["aws_sdk_omics.types.sample_id.SampleId"]
    """<p> The read set source's sample ID. </p>"""
    subject_id: NotRequired["aws_sdk_omics.types.subject_id.SubjectId"]
    """<p> The read set source's subject ID. </p>"""
    generated_from: NotRequired["aws_sdk_omics.types.generated_from.GeneratedFrom"]
    """<p> Where the source originated. </p>"""
    creation_type: NotRequired["aws_sdk_omics.types.creation_type.CreationType"]
    """<p> The creation type of the read set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    if "created_after" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["createdAfter"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["createdBefore"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["created_before"]
        )
    if "sample_id" in value:
        out["sampleId"] = value["sample_id"]
    if "subject_id" in value:
        out["subjectId"] = value["subject_id"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    if "creation_type" in value:
        out["creationType"] = value["creation_type"]
    return out


def deserialize_json(data: dict) -> ReadSetFilter:
    out: ReadSetFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "referenceArn" in data:
        out["reference_arn"] = data["referenceArn"]
    if "createdAfter" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["created_after"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["createdAfter"]
        )
    if "createdBefore" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["created_before"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["createdBefore"]
        )
    if "sampleId" in data:
        out["sample_id"] = data["sampleId"]
    if "subjectId" in data:
        out["subject_id"] = data["subjectId"]
    if "generatedFrom" in data:
        out["generated_from"] = data["generatedFrom"]
    if "creationType" in data:
        out["creation_type"] = data["creationType"]
    return out
