"""Generated from Smithy shape ``com.amazonaws.artifact#ReportDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_artifact.types.acceptance_type
    import aws_sdk_artifact.types.long_string_attribute
    import aws_sdk_artifact.types.published_state
    import aws_sdk_artifact.types.report_id
    import aws_sdk_artifact.types.sequence_number_attribute
    import aws_sdk_artifact.types.short_string_attribute
    import aws_sdk_artifact.types.status_message
    import aws_sdk_artifact.types.timestamp_attribute
    import aws_sdk_artifact.types.upload_state
    import aws_sdk_artifact.types.version_attribute


class ReportDetail(TypedDict):
    id: NotRequired["aws_sdk_artifact.types.report_id.ReportId"]
    """<p>Unique resource ID for the report resource.</p>"""
    name: NotRequired[
        "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Name for the report resource.</p>"""
    description: NotRequired[
        "aws_sdk_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Description for the report resource.</p>"""
    period_start: NotRequired[
        "aws_sdk_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating the report resource effective start.</p>"""
    period_end: NotRequired[
        "aws_sdk_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating the report resource effective end.</p>"""
    created_at: NotRequired[
        "aws_sdk_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the report resource was created.</p>"""
    last_modified_at: NotRequired[
        "aws_sdk_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the report resource was last modified.</p>"""
    deleted_at: NotRequired[
        "aws_sdk_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the report resource was deleted.</p>"""
    state: NotRequired["aws_sdk_artifact.types.published_state.PublishedState"]
    """<p>Current state of the report resource</p>"""
    arn: NotRequired["aws_sdk_artifact.types.long_string_attribute.LongStringAttribute"]
    """<p>ARN for the report resource.</p>"""
    series: NotRequired[
        "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Series for the report resource.</p>"""
    category: NotRequired[
        "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Category for the report resource.</p>"""
    company_name: NotRequired[
        "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Associated company name for the report resource.</p>"""
    product_name: NotRequired[
        "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Associated product name for the report resource.</p>"""
    term_arn: NotRequired[
        "aws_sdk_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Unique resource ARN for term resource.</p>"""
    version: NotRequired["aws_sdk_artifact.types.version_attribute.VersionAttribute"]
    """<p>Version for the report resource.</p>"""
    acceptance_type: NotRequired[
        "aws_sdk_artifact.types.acceptance_type.AcceptanceType"
    ]
    """<p>Acceptance type for report.</p>"""
    sequence_number: NotRequired[
        "aws_sdk_artifact.types.sequence_number_attribute.SequenceNumberAttribute"
    ]
    """<p>Sequence number to enforce optimistic locking.</p>"""
    upload_state: NotRequired["aws_sdk_artifact.types.upload_state.UploadState"]
    """<p>The current state of the document upload.</p>"""
    status_message: NotRequired["aws_sdk_artifact.types.status_message.StatusMessage"]
    """<p>The message associated with the current upload state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "period_start" in value:
        import aws_sdk_artifact.types.timestamp_attribute

        out["periodStart"] = aws_sdk_artifact.types.timestamp_attribute.serialize_json(
            value["period_start"]
        )
    if "period_end" in value:
        import aws_sdk_artifact.types.timestamp_attribute

        out["periodEnd"] = aws_sdk_artifact.types.timestamp_attribute.serialize_json(
            value["period_end"]
        )
    if "created_at" in value:
        import aws_sdk_artifact.types.timestamp_attribute

        out["createdAt"] = aws_sdk_artifact.types.timestamp_attribute.serialize_json(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import aws_sdk_artifact.types.timestamp_attribute

        out["lastModifiedAt"] = (
            aws_sdk_artifact.types.timestamp_attribute.serialize_json(
                value["last_modified_at"]
            )
        )
    if "deleted_at" in value:
        import aws_sdk_artifact.types.timestamp_attribute

        out["deletedAt"] = aws_sdk_artifact.types.timestamp_attribute.serialize_json(
            value["deleted_at"]
        )
    if "state" in value:
        import aws_sdk_artifact.types.published_state

        out["state"] = aws_sdk_artifact.types.published_state.serialize_json(
            value["state"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "series" in value:
        out["series"] = value["series"]
    if "category" in value:
        out["category"] = value["category"]
    if "company_name" in value:
        out["companyName"] = value["company_name"]
    if "product_name" in value:
        out["productName"] = value["product_name"]
    if "term_arn" in value:
        out["termArn"] = value["term_arn"]
    if "version" in value:
        out["version"] = value["version"]
    if "acceptance_type" in value:
        import aws_sdk_artifact.types.acceptance_type

        out["acceptanceType"] = aws_sdk_artifact.types.acceptance_type.serialize_json(
            value["acceptance_type"]
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    if "upload_state" in value:
        import aws_sdk_artifact.types.upload_state

        out["uploadState"] = aws_sdk_artifact.types.upload_state.serialize_json(
            value["upload_state"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ReportDetail:
    out: ReportDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "periodStart" in data:
        import aws_sdk_artifact.types.timestamp_attribute

        out["period_start"] = (
            aws_sdk_artifact.types.timestamp_attribute.deserialize_json(
                data["periodStart"]
            )
        )
    if "periodEnd" in data:
        import aws_sdk_artifact.types.timestamp_attribute

        out["period_end"] = aws_sdk_artifact.types.timestamp_attribute.deserialize_json(
            data["periodEnd"]
        )
    if "createdAt" in data:
        import aws_sdk_artifact.types.timestamp_attribute

        out["created_at"] = aws_sdk_artifact.types.timestamp_attribute.deserialize_json(
            data["createdAt"]
        )
    if "lastModifiedAt" in data:
        import aws_sdk_artifact.types.timestamp_attribute

        out["last_modified_at"] = (
            aws_sdk_artifact.types.timestamp_attribute.deserialize_json(
                data["lastModifiedAt"]
            )
        )
    if "deletedAt" in data:
        import aws_sdk_artifact.types.timestamp_attribute

        out["deleted_at"] = aws_sdk_artifact.types.timestamp_attribute.deserialize_json(
            data["deletedAt"]
        )
    if "state" in data:
        import aws_sdk_artifact.types.published_state

        out["state"] = aws_sdk_artifact.types.published_state.deserialize_json(
            data["state"]
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "series" in data:
        out["series"] = data["series"]
    if "category" in data:
        out["category"] = data["category"]
    if "companyName" in data:
        out["company_name"] = data["companyName"]
    if "productName" in data:
        out["product_name"] = data["productName"]
    if "termArn" in data:
        out["term_arn"] = data["termArn"]
    if "version" in data:
        out["version"] = data["version"]
    if "acceptanceType" in data:
        import aws_sdk_artifact.types.acceptance_type

        out["acceptance_type"] = (
            aws_sdk_artifact.types.acceptance_type.deserialize_json(
                data["acceptanceType"]
            )
        )
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    if "uploadState" in data:
        import aws_sdk_artifact.types.upload_state

        out["upload_state"] = aws_sdk_artifact.types.upload_state.deserialize_json(
            data["uploadState"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
