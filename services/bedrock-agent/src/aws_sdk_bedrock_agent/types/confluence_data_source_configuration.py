"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceDataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.confluence_crawler_configuration
    import aws_sdk_bedrock_agent.types.confluence_source_configuration


class ConfluenceDataSourceConfiguration(TypedDict, closed=True):
    source_configuration: "aws_sdk_bedrock_agent.types.confluence_source_configuration.ConfluenceSourceConfiguration"
    """<p>The endpoint information to connect to your Confluence data source.</p>"""
    crawler_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.confluence_crawler_configuration.ConfluenceCrawlerConfiguration"
    ]
    """<p>The configuration of the Confluence content. For example, configuring specific types of Confluence content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceDataSourceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.confluence_source_configuration

    out["sourceConfiguration"] = (
        aws_sdk_bedrock_agent.types.confluence_source_configuration.serialize_json(
            value["source_configuration"]
        )
    )
    if "crawler_configuration" in value:
        import aws_sdk_bedrock_agent.types.confluence_crawler_configuration

        out["crawlerConfiguration"] = (
            aws_sdk_bedrock_agent.types.confluence_crawler_configuration.serialize_json(
                value["crawler_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfluenceDataSourceConfiguration:
    out: ConfluenceDataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.confluence_source_configuration

        out["source_configuration"] = (
            aws_sdk_bedrock_agent.types.confluence_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ConfluenceDataSourceConfiguration.source_configuration required"
        )
    if "crawlerConfiguration" in data:
        import aws_sdk_bedrock_agent.types.confluence_crawler_configuration

        out["crawler_configuration"] = (
            aws_sdk_bedrock_agent.types.confluence_crawler_configuration.deserialize_json(
                data["crawlerConfiguration"]
            )
        )
    return out
