"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceCrawlerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.crawl_filter_configuration


class ConfluenceCrawlerConfiguration(TypedDict, closed=True):
    filter_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.crawl_filter_configuration.CrawlFilterConfiguration"
    ]
    """<p>The configuration of filtering the Confluence content. For example, configuring regular expression patterns to include or exclude certain content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceCrawlerConfiguration) -> dict:
    out: dict = {}
    if "filter_configuration" in value:
        import aws_sdk_bedrock_agent.types.crawl_filter_configuration

        out["filterConfiguration"] = (
            aws_sdk_bedrock_agent.types.crawl_filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfluenceCrawlerConfiguration:
    out: ConfluenceCrawlerConfiguration = {}  # type: ignore[typeddict-item]
    if "filterConfiguration" in data:
        import aws_sdk_bedrock_agent.types.crawl_filter_configuration

        out["filter_configuration"] = (
            aws_sdk_bedrock_agent.types.crawl_filter_configuration.deserialize_json(
                data["filterConfiguration"]
            )
        )
    return out
