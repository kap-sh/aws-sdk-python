"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteContinuousDeploymentPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DeleteContinuousDeploymentPolicyRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier of the continuous deployment policy that you are deleting.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version (<code>ETag</code> value) of the continuous deployment policy that you are deleting.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteContinuousDeploymentPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteContinuousDeploymentPolicyRequest:
    out: DeleteContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
