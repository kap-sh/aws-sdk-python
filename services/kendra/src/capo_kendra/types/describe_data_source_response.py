"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.custom_document_enrichment_configuration
    import capo_kendra.types.data_source_configuration
    import capo_kendra.types.data_source_id
    import capo_kendra.types.data_source_name
    import capo_kendra.types.data_source_status
    import capo_kendra.types.data_source_type
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.description
    import capo_kendra.types.error_message
    import capo_kendra.types.index_id
    import capo_kendra.types.language_code
    import capo_kendra.types.role_arn
    import capo_kendra.types.scan_schedule
    import capo_kendra.types.timestamp


class DescribeDataSourceResponse(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source connector.</p>"""
    index_id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index used with the data source connector.</p>"""
    name: NotRequired["capo_kendra.types.data_source_name.DataSourceName"]
    """<p>The name for the data source connector.</p>"""
    type: NotRequired["capo_kendra.types.data_source_type.DataSourceType"]
    """<p>The type of the data source. For example, <code>SHAREPOINT</code>.</p>"""
    configuration: NotRequired[
        "capo_kendra.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Configuration details for the data source connector. This shows how the data source is configured. The configuration options for a data source depend on the data source provider.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    r"""<p>Configuration information for an Amazon Virtual Private Cloud to connect to your data source. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html\">Configuring a VPC</a>.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the data source connector was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the data source connector was last updated.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>The description for the data source connector.</p>"""
    status: NotRequired["capo_kendra.types.data_source_status.DataSourceStatus"]
    """<p>The current status of the data source connector. When the status is <code>ACTIVE</code> the data source is ready to use. When the status is <code>FAILED</code>, the <code>ErrorMessage</code> field contains the reason that the data source failed.</p>"""
    schedule: NotRequired["capo_kendra.types.scan_schedule.ScanSchedule"]
    """<p>The schedule for Amazon Kendra to update the index.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role with permission to access the data source and required resources.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a description of the error that caused the data source to fail.</p>"""
    language_code: NotRequired["capo_kendra.types.language_code.LanguageCode"]
    r"""<p>The code for a language. This shows a supported language for all documents in the data source. English is supported by default. For more information on supported languages, including their codes, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html\">Adding documents in languages other than English</a>.</p>"""
    custom_document_enrichment_configuration: NotRequired[
        "capo_kendra.types.custom_document_enrichment_configuration.CustomDocumentEnrichmentConfiguration"
    ]
    r"""<p>Configuration information for altering document metadata and content during the document ingestion process when you describe a data source.</p> <p>For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html\">Customizing document metadata during the ingestion process</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataSourceResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "index_id" in value:
        out["IndexId"] = value["index_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_kendra.types.data_source_type

        out["Type"] = capo_kendra.types.data_source_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "configuration" in value:
        import capo_kendra.types.data_source_configuration

        out["Configuration"] = (
            capo_kendra.types.data_source_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "vpc_configuration" in value:
        import capo_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            capo_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_kendra.types.data_source_status

        out["Status"] = capo_kendra.types.data_source_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "custom_document_enrichment_configuration" in value:
        import capo_kendra.types.custom_document_enrichment_configuration

        out["CustomDocumentEnrichmentConfiguration"] = (
            capo_kendra.types.custom_document_enrichment_configuration.serialize_aws_json_1_1(
                value["custom_document_enrichment_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataSourceResponse:
    out: DescribeDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_kendra.types.data_source_type

        out["type"] = capo_kendra.types.data_source_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Configuration" in data:
        import capo_kendra.types.data_source_configuration

        out["configuration"] = (
            capo_kendra.types.data_source_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if "VpcConfiguration" in data:
        import capo_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if "CreatedAt" in data:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_kendra.types.data_source_status

        out["status"] = capo_kendra.types.data_source_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    if "CustomDocumentEnrichmentConfiguration" in data:
        import capo_kendra.types.custom_document_enrichment_configuration

        out["custom_document_enrichment_configuration"] = (
            capo_kendra.types.custom_document_enrichment_configuration.deserialize_aws_json_1_1(
                data["CustomDocumentEnrichmentConfiguration"]
            )
        )
    return out
