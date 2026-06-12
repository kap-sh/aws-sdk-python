"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistributionConfigWithTags``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.streaming_distribution_config
    import aws_sdk_cloudfront.types.tags


class StreamingDistributionConfigWithTags(TypedDict):
    streaming_distribution_config: "aws_sdk_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig"
    """<p>A streaming distribution Configuration.</p>"""
    tags: "aws_sdk_cloudfront.types.tags.Tags"
    """<p>A complex type that contains zero or more <code>Tag</code> elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StreamingDistributionConfigWithTags, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.streaming_distribution_config

    aws_sdk_cloudfront.types.streaming_distribution_config.serialize_xml(
        value["streaming_distribution_config"], el, "StreamingDistributionConfig"
    )
    import aws_sdk_cloudfront.types.tags

    aws_sdk_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> StreamingDistributionConfigWithTags:
    out: StreamingDistributionConfigWithTags = {}  # type: ignore[typeddict-item]
    child_streaming_distribution_config = el.find("StreamingDistributionConfig")
    if child_streaming_distribution_config is not None:
        import aws_sdk_cloudfront.types.streaming_distribution_config

        out["streaming_distribution_config"] = (
            aws_sdk_cloudfront.types.streaming_distribution_config.deserialize_xml(
                child_streaming_distribution_config
            )
        )
    else:
        raise DeserializationError(
            "StreamingDistributionConfigWithTags.streaming_distribution_config required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudfront.types.tags

        out["tags"] = aws_sdk_cloudfront.types.tags.deserialize_xml(child_tags)
    else:
        raise DeserializationError("StreamingDistributionConfigWithTags.tags required")
    return out
