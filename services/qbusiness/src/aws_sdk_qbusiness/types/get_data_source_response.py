"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_arn
    import aws_sdk_qbusiness.types.data_source_configuration
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.data_source_name
    import aws_sdk_qbusiness.types.data_source_status
    import aws_sdk_qbusiness.types.data_source_vpc_configuration
    import aws_sdk_qbusiness.types.description
    import aws_sdk_qbusiness.types.document_enrichment_configuration
    import aws_sdk_qbusiness.types.error_detail
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.media_extraction_configuration
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.sync_schedule
    import aws_sdk_qbusiness.types.timestamp


class GetDataSourceResponse(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application.</p>"""
    index_id: NotRequired["aws_sdk_qbusiness.types.index_id.IndexId"]
    """<p>The identifier of the index linked to the data source connector.</p>"""
    data_source_id: NotRequired["aws_sdk_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source connector.</p>"""
    data_source_arn: NotRequired[
        "aws_sdk_qbusiness.types.data_source_arn.DataSourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the data source.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.data_source_name.DataSourceName"]
    """<p>The name for the data source connector.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The type of the data source connector. For example, <code>S3</code>.</p>"""
    configuration: NotRequired[
        "aws_sdk_qbusiness.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>The details of how the data source connector is configured.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_qbusiness.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the data source connector was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the data source connector was last updated.</p>"""
    description: NotRequired["aws_sdk_qbusiness.types.description.Description"]
    """<p>The description for the data source connector.</p>"""
    status: NotRequired["aws_sdk_qbusiness.types.data_source_status.DataSourceStatus"]
    """<p>The current status of the data source connector. When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a description of the error that caused the data source connector to fail.</p>"""
    sync_schedule: NotRequired["aws_sdk_qbusiness.types.sync_schedule.SyncSchedule"]
    """<p>The schedule for Amazon Q Business to update the index.</p>"""
    role_arn: NotRequired["aws_sdk_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role with permission to access the data source and required resources.</p>"""
    error: NotRequired["aws_sdk_qbusiness.types.error_detail.ErrorDetail"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a description of the error that caused the data source connector to fail.</p>"""
    document_enrichment_configuration: NotRequired[
        "aws_sdk_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
    ]
    media_extraction_configuration: NotRequired[
        "aws_sdk_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The configuration for extracting information from media in documents for the data source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    if "data_source_arn" in value:
        out["dataSourceArn"] = value["data_source_arn"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "type" in value:
        out["type"] = value["type"]
    if "configuration" in value:
        out["configuration"] = value["configuration"]
    if "vpc_configuration" in value:
        import aws_sdk_qbusiness.types.data_source_vpc_configuration

        out["vpcConfiguration"] = (
            aws_sdk_qbusiness.types.data_source_vpc_configuration.serialize_json(
                value["vpc_configuration"]
            )
        )
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_qbusiness.types.data_source_status

        out["status"] = aws_sdk_qbusiness.types.data_source_status.serialize_json(
            value["status"]
        )
    if "sync_schedule" in value:
        out["syncSchedule"] = value["sync_schedule"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "error" in value:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.serialize_json(
            value["error"]
        )
    if "document_enrichment_configuration" in value:
        import aws_sdk_qbusiness.types.document_enrichment_configuration

        out["documentEnrichmentConfiguration"] = (
            aws_sdk_qbusiness.types.document_enrichment_configuration.serialize_json(
                value["document_enrichment_configuration"]
            )
        )
    if "media_extraction_configuration" in value:
        import aws_sdk_qbusiness.types.media_extraction_configuration

        out["mediaExtractionConfiguration"] = (
            aws_sdk_qbusiness.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataSourceResponse:
    out: GetDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "indexId" in data:
        out["index_id"] = data["indexId"]
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    if "dataSourceArn" in data:
        out["data_source_arn"] = data["dataSourceArn"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "type" in data:
        out["type"] = data["type"]
    if "configuration" in data:
        out["configuration"] = data["configuration"]
    if "vpcConfiguration" in data:
        import aws_sdk_qbusiness.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_qbusiness.types.data_source_vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_qbusiness.types.data_source_status

        out["status"] = aws_sdk_qbusiness.types.data_source_status.deserialize_json(
            data["status"]
        )
    if "syncSchedule" in data:
        out["sync_schedule"] = data["syncSchedule"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "error" in data:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.deserialize_json(
            data["error"]
        )
    if "documentEnrichmentConfiguration" in data:
        import aws_sdk_qbusiness.types.document_enrichment_configuration

        out["document_enrichment_configuration"] = (
            aws_sdk_qbusiness.types.document_enrichment_configuration.deserialize_json(
                data["documentEnrichmentConfiguration"]
            )
        )
    if "mediaExtractionConfiguration" in data:
        import aws_sdk_qbusiness.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            aws_sdk_qbusiness.types.media_extraction_configuration.deserialize_json(
                data["mediaExtractionConfiguration"]
            )
        )
    return out
