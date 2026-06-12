"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateStreamingDistributionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.streaming_distribution
    import aws_sdk_cloudfront.types.string


class UpdateStreamingDistributionResult(TypedDict):
    streaming_distribution: NotRequired[
        "aws_sdk_cloudfront.types.streaming_distribution.StreamingDistribution"
    ]
    """<p>The streaming distribution's information.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateStreamingDistributionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "streaming_distribution" in value:
        import aws_sdk_cloudfront.types.streaming_distribution

        aws_sdk_cloudfront.types.streaming_distribution.serialize_xml(
            value["streaming_distribution"], el, "StreamingDistribution"
        )


def deserialize_xml(el: Element) -> UpdateStreamingDistributionResult:
    out: UpdateStreamingDistributionResult = {}  # type: ignore[typeddict-item]
    child_streaming_distribution = el.find("StreamingDistribution")
    if child_streaming_distribution is not None:
        import aws_sdk_cloudfront.types.streaming_distribution

        out["streaming_distribution"] = (
            aws_sdk_cloudfront.types.streaming_distribution.deserialize_xml(
                child_streaming_distribution
            )
        )
    return out
