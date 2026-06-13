"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.data_set_status
    import aws_sdk_quicksight.types.data_source_arn
    import aws_sdk_quicksight.types.knowledge_base_arn
    import aws_sdk_quicksight.types.knowledge_base_configuration
    import aws_sdk_quicksight.types.knowledge_base_description
    import aws_sdk_quicksight.types.knowledge_base_id
    import aws_sdk_quicksight.types.knowledge_base_ingestion_summary
    import aws_sdk_quicksight.types.knowledge_base_name
    import aws_sdk_quicksight.types.long
    import aws_sdk_quicksight.types.media_extraction_configuration
    import aws_sdk_quicksight.types.sensitive_string


class KnowledgeBase(TypedDict):
    knowledge_base_arn: "aws_sdk_quicksight.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""
    name: "aws_sdk_quicksight.types.knowledge_base_name.KnowledgeBaseName"
    """<p>The name of the knowledge base.</p>"""
    status: "aws_sdk_quicksight.types.data_set_status.DataSetStatus"
    """<p>The status of the knowledge base.</p>"""
    data_source_arn: "aws_sdk_quicksight.types.data_source_arn.DataSourceArn"
    """<p>The ARN of the data source associated with the knowledge base.</p>"""
    knowledge_base_configuration: "aws_sdk_quicksight.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    """<p>The configuration settings for the knowledge base.</p>"""
    media_extraction_configuration: NotRequired[
        "aws_sdk_quicksight.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The media extraction configuration for the knowledge base.</p>"""
    type: NotRequired["str"]
    """<p>The type of the knowledge base.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the knowledge base was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the knowledge base was last updated.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.knowledge_base_description.KnowledgeBaseDescription"
    ]
    """<p>The description of the knowledge base.</p>"""
    is_email_notification_opted_for_ingestion_failures: NotRequired[
        "aws_sdk_quicksight.types.boolean.Boolean"
    ]
    """<p>Indicates whether email notifications are enabled for ingestion failures.</p>"""
    first_completed_ingestion_summary: NotRequired[
        "aws_sdk_quicksight.types.knowledge_base_ingestion_summary.KnowledgeBaseIngestionSummary"
    ]
    """<p>A summary of the first completed ingestion for the knowledge base.</p>"""
    first_incomplete_ingestion_summary: NotRequired[
        "aws_sdk_quicksight.types.knowledge_base_ingestion_summary.KnowledgeBaseIngestionSummary"
    ]
    """<p>A summary of the first incomplete ingestion for the knowledge base.</p>"""
    latest_ingestion_summary: NotRequired[
        "aws_sdk_quicksight.types.knowledge_base_ingestion_summary.KnowledgeBaseIngestionSummary"
    ]
    """<p>A summary of the most recent ingestion for the knowledge base.</p>"""
    knowledge_base_size_bytes: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The size of the knowledge base in bytes.</p>"""
    document_count: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The number of documents in the knowledge base.</p>"""
    primary_owner_arn: NotRequired["str"]
    """<p>The ARN of the primary owner of the knowledge base.</p>"""
    primary_owner_username: NotRequired[
        "aws_sdk_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The username of the primary owner of the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBase) -> dict:
    out: dict = {}
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.data_set_status

    out["Status"] = aws_sdk_quicksight.types.data_set_status.serialize_json(
        value["status"]
    )
    out["DataSourceArn"] = value["data_source_arn"]
    import aws_sdk_quicksight.types.knowledge_base_configuration

    out["KnowledgeBaseConfiguration"] = (
        aws_sdk_quicksight.types.knowledge_base_configuration.serialize_json(
            value["knowledge_base_configuration"]
        )
    )
    if "media_extraction_configuration" in value:
        import aws_sdk_quicksight.types.media_extraction_configuration

        out["MediaExtractionConfiguration"] = (
            aws_sdk_quicksight.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    if "created_at" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["CreatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["UpdatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "is_email_notification_opted_for_ingestion_failures" in value:
        out["IsEmailNotificationOptedForIngestionFailures"] = value[
            "is_email_notification_opted_for_ingestion_failures"
        ]
    if "first_completed_ingestion_summary" in value:
        import aws_sdk_quicksight.types.knowledge_base_ingestion_summary

        out["FirstCompletedIngestionSummary"] = (
            aws_sdk_quicksight.types.knowledge_base_ingestion_summary.serialize_json(
                value["first_completed_ingestion_summary"]
            )
        )
    if "first_incomplete_ingestion_summary" in value:
        import aws_sdk_quicksight.types.knowledge_base_ingestion_summary

        out["FirstIncompleteIngestionSummary"] = (
            aws_sdk_quicksight.types.knowledge_base_ingestion_summary.serialize_json(
                value["first_incomplete_ingestion_summary"]
            )
        )
    if "latest_ingestion_summary" in value:
        import aws_sdk_quicksight.types.knowledge_base_ingestion_summary

        out["LatestIngestionSummary"] = (
            aws_sdk_quicksight.types.knowledge_base_ingestion_summary.serialize_json(
                value["latest_ingestion_summary"]
            )
        )
    if "knowledge_base_size_bytes" in value:
        out["KnowledgeBaseSizeBytes"] = value["knowledge_base_size_bytes"]
    if "document_count" in value:
        out["DocumentCount"] = value["document_count"]
    if "primary_owner_arn" in value:
        out["PrimaryOwnerArn"] = value["primary_owner_arn"]
    if "primary_owner_username" in value:
        out["PrimaryOwnerUsername"] = value["primary_owner_username"]
    return out


def deserialize_json(data: dict) -> KnowledgeBase:
    out: KnowledgeBase = {}  # type: ignore[typeddict-item]
    if "KnowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        raise DeserializationError("KnowledgeBase.knowledge_base_arn required")
    if "KnowledgeBaseId" in data:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBase.knowledge_base_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("KnowledgeBase.name required")
    if "Status" in data:
        import aws_sdk_quicksight.types.data_set_status

        out["status"] = aws_sdk_quicksight.types.data_set_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("KnowledgeBase.status required")
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("KnowledgeBase.data_source_arn required")
    if "KnowledgeBaseConfiguration" in data:
        import aws_sdk_quicksight.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            aws_sdk_quicksight.types.knowledge_base_configuration.deserialize_json(
                data["KnowledgeBaseConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBase.knowledge_base_configuration required"
        )
    if "MediaExtractionConfiguration" in data:
        import aws_sdk_quicksight.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            aws_sdk_quicksight.types.media_extraction_configuration.deserialize_json(
                data["MediaExtractionConfiguration"]
            )
        )
    if "Type" in data:
        out["type"] = data["Type"]
    if "CreatedAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "IsEmailNotificationOptedForIngestionFailures" in data:
        out["is_email_notification_opted_for_ingestion_failures"] = data[
            "IsEmailNotificationOptedForIngestionFailures"
        ]
    if "FirstCompletedIngestionSummary" in data:
        import aws_sdk_quicksight.types.knowledge_base_ingestion_summary

        out["first_completed_ingestion_summary"] = (
            aws_sdk_quicksight.types.knowledge_base_ingestion_summary.deserialize_json(
                data["FirstCompletedIngestionSummary"]
            )
        )
    if "FirstIncompleteIngestionSummary" in data:
        import aws_sdk_quicksight.types.knowledge_base_ingestion_summary

        out["first_incomplete_ingestion_summary"] = (
            aws_sdk_quicksight.types.knowledge_base_ingestion_summary.deserialize_json(
                data["FirstIncompleteIngestionSummary"]
            )
        )
    if "LatestIngestionSummary" in data:
        import aws_sdk_quicksight.types.knowledge_base_ingestion_summary

        out["latest_ingestion_summary"] = (
            aws_sdk_quicksight.types.knowledge_base_ingestion_summary.deserialize_json(
                data["LatestIngestionSummary"]
            )
        )
    if "KnowledgeBaseSizeBytes" in data:
        out["knowledge_base_size_bytes"] = data["KnowledgeBaseSizeBytes"]
    if "DocumentCount" in data:
        out["document_count"] = data["DocumentCount"]
    if "PrimaryOwnerArn" in data:
        out["primary_owner_arn"] = data["PrimaryOwnerArn"]
    if "PrimaryOwnerUsername" in data:
        out["primary_owner_username"] = data["PrimaryOwnerUsername"]
    return out
