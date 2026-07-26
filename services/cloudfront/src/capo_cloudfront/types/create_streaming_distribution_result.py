"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateStreamingDistributionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.streaming_distribution
    import capo_cloudfront.types.string


class CreateStreamingDistributionResult(TypedDict, closed=True):
    streaming_distribution: NotRequired[
        "capo_cloudfront.types.streaming_distribution.StreamingDistribution"
    ]
    """<p>The streaming distribution's information.</p>"""
    location: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The fully qualified URI of the new streaming distribution resource just created.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the streaming distribution created.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateStreamingDistributionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "streaming_distribution" in value:
        import capo_cloudfront.types.streaming_distribution

        capo_cloudfront.types.streaming_distribution.serialize_xml(
            value["streaming_distribution"], el, "StreamingDistribution"
        )


def deserialize_xml(el: Element) -> CreateStreamingDistributionResult:
    out: CreateStreamingDistributionResult = {}  # type: ignore[typeddict-item]
    child_streaming_distribution = el.find("StreamingDistribution")
    if child_streaming_distribution is not None:
        import capo_cloudfront.types.streaming_distribution

        out["streaming_distribution"] = (
            capo_cloudfront.types.streaming_distribution.deserialize_xml(
                child_streaming_distribution
            )
        )
    return out
