"""Generated from Smithy shape ``com.amazonaws.cloudfront#AssociateDistributionTenantWebACLResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class AssociateDistributionTenantWebACLResult(TypedDict, closed=True):
    id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The ID of the distribution tenant.</p>"""
    web_acl_arn: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The ARN of the WAF web ACL that you associated with the distribution tenant.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AssociateDistributionTenantWebACLResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    if "web_acl_arn" in value:
        SubElement(el, "WebACLArn").text = str(value["web_acl_arn"])


def deserialize_xml(el: Element) -> AssociateDistributionTenantWebACLResult:
    out: AssociateDistributionTenantWebACLResult = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_web_acl_arn = el.find("WebACLArn")
    if child_web_acl_arn is not None:
        out["web_acl_arn"] = str(child_web_acl_arn.text or "")
    return out
