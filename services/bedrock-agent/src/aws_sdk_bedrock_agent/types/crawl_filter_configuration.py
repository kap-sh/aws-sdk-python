"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CrawlFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.crawl_filter_configuration_type
    import aws_sdk_bedrock_agent.types.pattern_object_filter_configuration


class CrawlFilterConfiguration(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent.types.crawl_filter_configuration_type.CrawlFilterConfigurationType"
    """<p>The type of filtering that you want to apply to certain objects or content of the data source. For example, the <code>PATTERN</code> type is regular expression patterns you can apply to filter your content.</p>"""
    pattern_object_filter: NotRequired[
        "aws_sdk_bedrock_agent.types.pattern_object_filter_configuration.PatternObjectFilterConfiguration"
    ]
    """<p>The configuration of filtering certain objects or content types of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrawlFilterConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.crawl_filter_configuration_type

    out["type"] = (
        aws_sdk_bedrock_agent.types.crawl_filter_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "pattern_object_filter" in value:
        import aws_sdk_bedrock_agent.types.pattern_object_filter_configuration

        out["patternObjectFilter"] = (
            aws_sdk_bedrock_agent.types.pattern_object_filter_configuration.serialize_json(
                value["pattern_object_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> CrawlFilterConfiguration:
    out: CrawlFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.crawl_filter_configuration_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.crawl_filter_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("CrawlFilterConfiguration.type required")
    if "patternObjectFilter" in data:
        import aws_sdk_bedrock_agent.types.pattern_object_filter_configuration

        out["pattern_object_filter"] = (
            aws_sdk_bedrock_agent.types.pattern_object_filter_configuration.deserialize_json(
                data["patternObjectFilter"]
            )
        )
    return out
