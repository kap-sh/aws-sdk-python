"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetContinuousDeploymentPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetContinuousDeploymentPolicyRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the continuous deployment policy that you are getting.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetContinuousDeploymentPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetContinuousDeploymentPolicyRequest:
    out: GetContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
