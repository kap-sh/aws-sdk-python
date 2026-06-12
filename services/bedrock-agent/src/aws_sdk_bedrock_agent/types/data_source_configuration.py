"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.confluence_data_source_configuration
    import aws_sdk_bedrock_agent.types.data_source_type
    import aws_sdk_bedrock_agent.types.s3_data_source_configuration
    import aws_sdk_bedrock_agent.types.salesforce_data_source_configuration
    import aws_sdk_bedrock_agent.types.share_point_data_source_configuration
    import aws_sdk_bedrock_agent.types.web_data_source_configuration


class DataSourceConfiguration(TypedDict):
    type: "aws_sdk_bedrock_agent.types.data_source_type.DataSourceType"
    """<p>The type of data source.</p>"""
    s3_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.s3_data_source_configuration.S3DataSourceConfiguration"
    ]
    """<p>The configuration information to connect to Amazon S3 as your data source.</p>"""
    web_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.web_data_source_configuration.WebDataSourceConfiguration"
    ]
    """<p>The configuration of web URLs to crawl for your data source. You should be authorized to crawl the URLs.</p> <note> <p>Crawling web URLs as your data source is in preview release and is subject to change.</p> </note>"""
    confluence_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.confluence_data_source_configuration.ConfluenceDataSourceConfiguration"
    ]
    """<p>The configuration information to connect to Confluence as your data source.</p> <note> <p>Confluence data source connector is in preview release and is subject to change.</p> </note>"""
    salesforce_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.salesforce_data_source_configuration.SalesforceDataSourceConfiguration"
    ]
    """<p>The configuration information to connect to Salesforce as your data source.</p> <note> <p>Salesforce data source connector is in preview release and is subject to change.</p> </note>"""
    share_point_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.share_point_data_source_configuration.SharePointDataSourceConfiguration"
    ]
    """<p>The configuration information to connect to SharePoint as your data source.</p> <note> <p>SharePoint data source connector is in preview release and is subject to change.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.data_source_type

    out["type"] = aws_sdk_bedrock_agent.types.data_source_type.serialize_json(
        value["type"]
    )
    if "s3_configuration" in value:
        import aws_sdk_bedrock_agent.types.s3_data_source_configuration

        out["s3Configuration"] = (
            aws_sdk_bedrock_agent.types.s3_data_source_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    if "web_configuration" in value:
        import aws_sdk_bedrock_agent.types.web_data_source_configuration

        out["webConfiguration"] = (
            aws_sdk_bedrock_agent.types.web_data_source_configuration.serialize_json(
                value["web_configuration"]
            )
        )
    if "confluence_configuration" in value:
        import aws_sdk_bedrock_agent.types.confluence_data_source_configuration

        out["confluenceConfiguration"] = (
            aws_sdk_bedrock_agent.types.confluence_data_source_configuration.serialize_json(
                value["confluence_configuration"]
            )
        )
    if "salesforce_configuration" in value:
        import aws_sdk_bedrock_agent.types.salesforce_data_source_configuration

        out["salesforceConfiguration"] = (
            aws_sdk_bedrock_agent.types.salesforce_data_source_configuration.serialize_json(
                value["salesforce_configuration"]
            )
        )
    if "share_point_configuration" in value:
        import aws_sdk_bedrock_agent.types.share_point_data_source_configuration

        out["sharePointConfiguration"] = (
            aws_sdk_bedrock_agent.types.share_point_data_source_configuration.serialize_json(
                value["share_point_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceConfiguration:
    out: DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.data_source_type

        out["type"] = aws_sdk_bedrock_agent.types.data_source_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("DataSourceConfiguration.type required")
    if "s3Configuration" in data:
        import aws_sdk_bedrock_agent.types.s3_data_source_configuration

        out["s3_configuration"] = (
            aws_sdk_bedrock_agent.types.s3_data_source_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    if "webConfiguration" in data:
        import aws_sdk_bedrock_agent.types.web_data_source_configuration

        out["web_configuration"] = (
            aws_sdk_bedrock_agent.types.web_data_source_configuration.deserialize_json(
                data["webConfiguration"]
            )
        )
    if "confluenceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.confluence_data_source_configuration

        out["confluence_configuration"] = (
            aws_sdk_bedrock_agent.types.confluence_data_source_configuration.deserialize_json(
                data["confluenceConfiguration"]
            )
        )
    if "salesforceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.salesforce_data_source_configuration

        out["salesforce_configuration"] = (
            aws_sdk_bedrock_agent.types.salesforce_data_source_configuration.deserialize_json(
                data["salesforceConfiguration"]
            )
        )
    if "sharePointConfiguration" in data:
        import aws_sdk_bedrock_agent.types.share_point_data_source_configuration

        out["share_point_configuration"] = (
            aws_sdk_bedrock_agent.types.share_point_data_source_configuration.deserialize_json(
                data["sharePointConfiguration"]
            )
        )
    return out
