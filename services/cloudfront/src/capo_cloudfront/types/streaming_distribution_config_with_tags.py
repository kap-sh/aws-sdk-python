"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistributionConfigWithTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.streaming_distribution_config
    import capo_cloudfront.types.tags


class StreamingDistributionConfigWithTags(TypedDict, closed=True):
    streaming_distribution_config: "capo_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig"
    """<p>A streaming distribution Configuration.</p>"""
    tags: "capo_cloudfront.types.tags.Tags"
    """<p>A complex type that contains zero or more <code>Tag</code> elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StreamingDistributionConfigWithTags, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.streaming_distribution_config

    capo_cloudfront.types.streaming_distribution_config.serialize_xml(
        value["streaming_distribution_config"], el, "StreamingDistributionConfig"
    )
    import capo_cloudfront.types.tags

    capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> StreamingDistributionConfigWithTags:
    out: StreamingDistributionConfigWithTags = {}  # type: ignore[typeddict-item]
    child_streaming_distribution_config = el.find("StreamingDistributionConfig")
    if child_streaming_distribution_config is not None:
        import capo_cloudfront.types.streaming_distribution_config

        out["streaming_distribution_config"] = (
            capo_cloudfront.types.streaming_distribution_config.deserialize_xml(
                child_streaming_distribution_config
            )
        )
    else:
        raise DeserializationError(
            "StreamingDistributionConfigWithTags.streaming_distribution_config required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    else:
        raise DeserializationError("StreamingDistributionConfigWithTags.tags required")
    return out
