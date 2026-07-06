"""Generated from Smithy shape ``com.amazonaws.cloudfront#AssociateDistributionTenantWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class AssociateDistributionTenantWebACLRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution tenant.</p>"""
    web_acl_arn: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the WAF web ACL to associate.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current <code>ETag</code> of the distribution tenant. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AssociateDistributionTenantWebACLRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "WebACLArn").text = str(value["web_acl_arn"])


def deserialize_xml(el: Element) -> AssociateDistributionTenantWebACLRequest:
    out: AssociateDistributionTenantWebACLRequest = {}  # type: ignore[typeddict-item]
    child_web_acl_arn = el.find("WebACLArn")
    if child_web_acl_arn is not None:
        out["web_acl_arn"] = str(child_web_acl_arn.text or "")
    else:
        raise DeserializationError(
            "AssociateDistributionTenantWebACLRequest.web_acl_arn required"
        )
    return out
