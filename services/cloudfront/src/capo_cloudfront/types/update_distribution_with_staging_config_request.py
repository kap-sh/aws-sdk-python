"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateDistributionWithStagingConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class UpdateDistributionWithStagingConfigRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier of the primary distribution to which you are copying a staging distribution's configuration.</p>"""
    staging_distribution_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The identifier of the staging distribution whose configuration you are copying to the primary distribution.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current versions (<code>ETag</code> values) of both primary and staging distributions. Provide these in the following format:</p> <p> <code>&lt;primary ETag&gt;, &lt;staging ETag&gt;</code> </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateDistributionWithStagingConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> UpdateDistributionWithStagingConfigRequest:
    out: UpdateDistributionWithStagingConfigRequest = {}  # type: ignore[typeddict-item]
    return out
