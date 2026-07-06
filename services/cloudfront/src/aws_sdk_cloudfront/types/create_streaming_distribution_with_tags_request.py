"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateStreamingDistributionWithTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.streaming_distribution_config_with_tags


class CreateStreamingDistributionWithTagsRequest(TypedDict, closed=True):
    streaming_distribution_config_with_tags: "aws_sdk_cloudfront.types.streaming_distribution_config_with_tags.StreamingDistributionConfigWithTags"
    """<p>The streaming distribution's configuration information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateStreamingDistributionWithTagsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.streaming_distribution_config_with_tags

    aws_sdk_cloudfront.types.streaming_distribution_config_with_tags.serialize_xml(
        value["streaming_distribution_config_with_tags"],
        el,
        "StreamingDistributionConfigWithTags",
    )


def deserialize_xml(el: Element) -> CreateStreamingDistributionWithTagsRequest:
    out: CreateStreamingDistributionWithTagsRequest = {}  # type: ignore[typeddict-item]
    child_streaming_distribution_config_with_tags = el.find(
        "StreamingDistributionConfigWithTags"
    )
    if child_streaming_distribution_config_with_tags is not None:
        import aws_sdk_cloudfront.types.streaming_distribution_config_with_tags

        out["streaming_distribution_config_with_tags"] = (
            aws_sdk_cloudfront.types.streaming_distribution_config_with_tags.deserialize_xml(
                child_streaming_distribution_config_with_tags
            )
        )
    else:
        raise DeserializationError(
            "CreateStreamingDistributionWithTagsRequest.streaming_distribution_config_with_tags required"
        )
    return out
