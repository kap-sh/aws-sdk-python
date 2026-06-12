"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SalesforceDataSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.salesforce_crawler_configuration
    import aws_sdk_bedrock_agent.types.salesforce_source_configuration


class SalesforceDataSourceConfiguration(TypedDict):
    source_configuration: "aws_sdk_bedrock_agent.types.salesforce_source_configuration.SalesforceSourceConfiguration"
    """<p>The endpoint information to connect to your Salesforce data source.</p>"""
    crawler_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.salesforce_crawler_configuration.SalesforceCrawlerConfiguration"
    ]
    """<p>The configuration of the Salesforce content. For example, configuring specific types of Salesforce content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceDataSourceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.salesforce_source_configuration

    out["sourceConfiguration"] = (
        aws_sdk_bedrock_agent.types.salesforce_source_configuration.serialize_json(
            value["source_configuration"]
        )
    )
    if "crawler_configuration" in value:
        import aws_sdk_bedrock_agent.types.salesforce_crawler_configuration

        out["crawlerConfiguration"] = (
            aws_sdk_bedrock_agent.types.salesforce_crawler_configuration.serialize_json(
                value["crawler_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SalesforceDataSourceConfiguration:
    out: SalesforceDataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.salesforce_source_configuration

        out["source_configuration"] = (
            aws_sdk_bedrock_agent.types.salesforce_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SalesforceDataSourceConfiguration.source_configuration required"
        )
    if "crawlerConfiguration" in data:
        import aws_sdk_bedrock_agent.types.salesforce_crawler_configuration

        out["crawler_configuration"] = (
            aws_sdk_bedrock_agent.types.salesforce_crawler_configuration.deserialize_json(
                data["crawlerConfiguration"]
            )
        )
    return out
