"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateStreamingDistributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.streaming_distribution_config


class CreateStreamingDistributionRequest(TypedDict, closed=True):
    streaming_distribution_config: "aws_sdk_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig"
    """<p>The streaming distribution's configuration information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateStreamingDistributionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.streaming_distribution_config

    aws_sdk_cloudfront.types.streaming_distribution_config.serialize_xml(
        value["streaming_distribution_config"], el, "StreamingDistributionConfig"
    )


def deserialize_xml(el: Element) -> CreateStreamingDistributionRequest:
    out: CreateStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
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
            "CreateStreamingDistributionRequest.streaming_distribution_config required"
        )
    return out
