"""Generated from Smithy shape ``com.amazonaws.kendra#CreateDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.client_token_name
    import aws_sdk_kendra.types.custom_document_enrichment_configuration
    import aws_sdk_kendra.types.data_source_configuration
    import aws_sdk_kendra.types.data_source_name
    import aws_sdk_kendra.types.data_source_type
    import aws_sdk_kendra.types.data_source_vpc_configuration
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.language_code
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.scan_schedule
    import aws_sdk_kendra.types.tag_list


class CreateDataSourceRequest(TypedDict):
    name: "aws_sdk_kendra.types.data_source_name.DataSourceName"
    """<p>A name for the data source connector.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to use with the data source connector.</p>"""
    type: "aws_sdk_kendra.types.data_source_type.DataSourceType"
    """<p>The type of data source repository. For example, <code>SHAREPOINT</code>.</p>"""
    configuration: NotRequired[
        "aws_sdk_kendra.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Configuration information to connect to your data source repository.</p> <p>You can't specify the <code>Configuration</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception.</p> <p>The <code>Configuration</code> parameter is required for all other data sources.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    r"""<p>Configuration information for an Amazon Virtual Private Cloud to connect to your data source. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html\">Configuring a VPC</a>.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A description for the data source connector.</p>"""
    schedule: NotRequired["aws_sdk_kendra.types.scan_schedule.ScanSchedule"]
    """<p>Sets the frequency for Amazon Kendra to check the documents in your data source repository and update the index. If you don't set a schedule Amazon Kendra will not periodically update the index. You can call the <code>StartDataSourceSyncJob</code> API to update the index.</p> <p>Specify a <code>cron-</code> format schedule string or an empty string to indicate that the index is updated on demand.</p> <p>You can't specify the <code>Schedule</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html\">IAM access roles for Amazon Kendra.</a>.</p> <p>You can't specify the <code>RoleArn</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception.</p> <p>The <code>RoleArn</code> parameter is required for all other data sources.</p>"""
    tags: NotRequired["aws_sdk_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    client_token: NotRequired["aws_sdk_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create a data source connector. Multiple calls to the <code>CreateDataSource</code> API with the same client token will create only one data source connector.</p>"""
    language_code: NotRequired["aws_sdk_kendra.types.language_code.LanguageCode"]
    r"""<p>The code for a language. This allows you to support a language for all documents when creating the data source connector. English is supported by default. For more information on supported languages, including their codes, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html\">Adding documents in languages other than English</a>.</p>"""
    custom_document_enrichment_configuration: NotRequired[
        "aws_sdk_kendra.types.custom_document_enrichment_configuration.CustomDocumentEnrichmentConfiguration"
    ]
    r"""<p>Configuration information for altering document metadata and content during the document ingestion process.</p> <p>For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html\">Customizing document metadata during the ingestion process</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["IndexId"] = value["index_id"]
    import aws_sdk_kendra.types.data_source_type

    out["Type"] = aws_sdk_kendra.types.data_source_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "configuration" in value:
        import aws_sdk_kendra.types.data_source_configuration

        out["Configuration"] = (
            aws_sdk_kendra.types.data_source_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "vpc_configuration" in value:
        import aws_sdk_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            aws_sdk_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_kendra.types.tag_list

        out["Tags"] = aws_sdk_kendra.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "custom_document_enrichment_configuration" in value:
        import aws_sdk_kendra.types.custom_document_enrichment_configuration

        out["CustomDocumentEnrichmentConfiguration"] = (
            aws_sdk_kendra.types.custom_document_enrichment_configuration.serialize_aws_json_1_1(
                value["custom_document_enrichment_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceRequest:
    out: CreateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataSourceRequest.name required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("CreateDataSourceRequest.index_id required")
    if "Type" in data:
        import aws_sdk_kendra.types.data_source_type

        out["type"] = aws_sdk_kendra.types.data_source_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateDataSourceRequest.type required")
    if "Configuration" in data:
        import aws_sdk_kendra.types.data_source_configuration

        out["configuration"] = (
            aws_sdk_kendra.types.data_source_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if "VpcConfiguration" in data:
        import aws_sdk_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import aws_sdk_kendra.types.tag_list

        out["tags"] = aws_sdk_kendra.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    if "CustomDocumentEnrichmentConfiguration" in data:
        import aws_sdk_kendra.types.custom_document_enrichment_configuration

        out["custom_document_enrichment_configuration"] = (
            aws_sdk_kendra.types.custom_document_enrichment_configuration.deserialize_aws_json_1_1(
                data["CustomDocumentEnrichmentConfiguration"]
            )
        )
    return out
