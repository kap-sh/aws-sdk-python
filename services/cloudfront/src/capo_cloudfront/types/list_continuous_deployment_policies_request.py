"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListContinuousDeploymentPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ListContinuousDeploymentPoliciesRequest(TypedDict, closed=True):
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The maximum number of continuous deployment policies that you want returned in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListContinuousDeploymentPoliciesRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListContinuousDeploymentPoliciesRequest:
    out: ListContinuousDeploymentPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
