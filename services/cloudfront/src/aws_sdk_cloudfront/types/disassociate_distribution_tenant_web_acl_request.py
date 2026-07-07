"""Generated from Smithy shape ``com.amazonaws.cloudfront#DisassociateDistributionTenantWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DisassociateDistributionTenantWebACLRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution tenant.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the distribution tenant that you're disassociating from the WAF web ACL. This is the <code>ETag</code> value returned in the response to the <code>GetDistributionTenant</code> API operation.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DisassociateDistributionTenantWebACLRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DisassociateDistributionTenantWebACLRequest:
    out: DisassociateDistributionTenantWebACLRequest = {}  # type: ignore[typeddict-item]
    return out
