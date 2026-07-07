"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetContinuousDeploymentPolicyConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetContinuousDeploymentPolicyConfigRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the continuous deployment policy whose configuration you are getting.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetContinuousDeploymentPolicyConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetContinuousDeploymentPolicyConfigRequest:
    out: GetContinuousDeploymentPolicyConfigRequest = {}  # type: ignore[typeddict-item]
    return out
