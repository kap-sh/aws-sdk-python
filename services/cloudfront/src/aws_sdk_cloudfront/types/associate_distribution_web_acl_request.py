"""Generated from Smithy shape ``com.amazonaws.cloudfront#AssociateDistributionWebACLRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class AssociateDistributionWebACLRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution.</p>"""
    web_acl_arn: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the WAF web ACL to associate.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the distribution that you're associating with the WAF web ACL.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AssociateDistributionWebACLRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "WebACLArn").text = str(value["web_acl_arn"])


def deserialize_xml(el: Element) -> AssociateDistributionWebACLRequest:
    out: AssociateDistributionWebACLRequest = {}  # type: ignore[typeddict-item]
    child_web_acl_arn = el.find("WebACLArn")
    if child_web_acl_arn is not None:
        out["web_acl_arn"] = str(child_web_acl_arn.text or "")
    else:
        raise DeserializationError(
            "AssociateDistributionWebACLRequest.web_acl_arn required"
        )
    return out
