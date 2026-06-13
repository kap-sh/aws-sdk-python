"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_configuration
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.data_source_name
    import aws_sdk_qbusiness.types.data_source_vpc_configuration
    import aws_sdk_qbusiness.types.description
    import aws_sdk_qbusiness.types.document_enrichment_configuration
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.media_extraction_configuration
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.sync_schedule


class UpdateDataSourceRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p> The identifier of the Amazon Q Business application the data source is attached to.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index attached to the data source connector.</p>"""
    data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.data_source_name.DataSourceName"]
    """<p>A name of the data source connector.</p>"""
    configuration: NotRequired[
        "aws_sdk_qbusiness.types.data_source_configuration.DataSourceConfiguration"
    ]
    vpc_configuration: NotRequired[
        "aws_sdk_qbusiness.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    description: NotRequired["aws_sdk_qbusiness.types.description.Description"]
    """<p>The description of the data source connector.</p>"""
    sync_schedule: NotRequired["aws_sdk_qbusiness.types.sync_schedule.SyncSchedule"]
    """<p>The chosen update frequency for your data source.</p>"""
    role_arn: NotRequired["aws_sdk_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.</p>"""
    document_enrichment_configuration: NotRequired[
        "aws_sdk_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
    ]
    media_extraction_configuration: NotRequired[
        "aws_sdk_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The configuration for extracting information from media in documents for your data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "configuration" in value:
        out["configuration"] = value["configuration"]
    if "vpc_configuration" in value:
        import aws_sdk_qbusiness.types.data_source_vpc_configuration

        out["vpcConfiguration"] = (
            aws_sdk_qbusiness.types.data_source_vpc_configuration.serialize_json(
                value["vpc_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "sync_schedule" in value:
        out["syncSchedule"] = value["sync_schedule"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
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


def deserialize_json(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "configuration" in data:
        out["configuration"] = data["configuration"]
    if "vpcConfiguration" in data:
        import aws_sdk_qbusiness.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_qbusiness.types.data_source_vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "syncSchedule" in data:
        out["sync_schedule"] = data["syncSchedule"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
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
