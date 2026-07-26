"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetResourcePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetResourcePolicyResult(TypedDict, closed=True):
    resource_arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the CloudFront resource that is associated with the resource policy.</p>"""
    policy_document: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The resource policy in JSON format.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetResourcePolicyResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "resource_arn" in value:
        SubElement(el, "ResourceArn").text = str(value["resource_arn"])
    if "policy_document" in value:
        SubElement(el, "PolicyDocument").text = str(value["policy_document"])


def deserialize_xml(el: Element) -> GetResourcePolicyResult:
    out: GetResourcePolicyResult = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    return out
