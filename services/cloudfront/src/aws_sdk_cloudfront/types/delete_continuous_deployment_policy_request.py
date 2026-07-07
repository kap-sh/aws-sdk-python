"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteContinuousDeploymentPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteContinuousDeploymentPolicyRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the continuous deployment policy that you are deleting.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version (<code>ETag</code> value) of the continuous deployment policy that you are deleting.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteContinuousDeploymentPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteContinuousDeploymentPolicyRequest:
    out: DeleteContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
