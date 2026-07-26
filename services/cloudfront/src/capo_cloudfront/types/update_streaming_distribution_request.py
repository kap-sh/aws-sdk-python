"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateStreamingDistributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.streaming_distribution_config
    import capo_cloudfront.types.string


class UpdateStreamingDistributionRequest(TypedDict, closed=True):
    streaming_distribution_config: "capo_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig"
    """<p>The streaming distribution's configuration information.</p>"""
    id: "capo_cloudfront.types.string.string"
    """<p>The streaming distribution's id.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateStreamingDistributionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.streaming_distribution_config

    capo_cloudfront.types.streaming_distribution_config.serialize_xml(
        value["streaming_distribution_config"], el, "StreamingDistributionConfig"
    )


def deserialize_xml(el: Element) -> UpdateStreamingDistributionRequest:
    out: UpdateStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
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
            "UpdateStreamingDistributionRequest.streaming_distribution_config required"
        )
    return out
