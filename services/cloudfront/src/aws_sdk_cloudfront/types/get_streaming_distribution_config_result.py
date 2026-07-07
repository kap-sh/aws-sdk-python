"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetStreamingDistributionConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.streaming_distribution_config
    import aws_sdk_cloudfront.types.string


class GetStreamingDistributionConfigResult(TypedDict, closed=True):
    streaming_distribution_config: NotRequired[
        "aws_sdk_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig"
    ]
    """<p>The streaming distribution's configuration information.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the configuration. For example: <code>E2QWRUHAPOMQZL</code>. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetStreamingDistributionConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "streaming_distribution_config" in value:
        import aws_sdk_cloudfront.types.streaming_distribution_config

        aws_sdk_cloudfront.types.streaming_distribution_config.serialize_xml(
            value["streaming_distribution_config"], el, "StreamingDistributionConfig"
        )


def deserialize_xml(el: Element) -> GetStreamingDistributionConfigResult:
    out: GetStreamingDistributionConfigResult = {}  # type: ignore[typeddict-item]
    child_streaming_distribution_config = el.find("StreamingDistributionConfig")
    if child_streaming_distribution_config is not None:
        import aws_sdk_cloudfront.types.streaming_distribution_config

        out["streaming_distribution_config"] = (
            aws_sdk_cloudfront.types.streaming_distribution_config.deserialize_xml(
                child_streaming_distribution_config
            )
        )
    return out
