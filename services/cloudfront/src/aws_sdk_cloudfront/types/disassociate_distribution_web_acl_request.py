"""Generated from Smithy shape ``com.amazonaws.cloudfront#DisassociateDistributionWebACLRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DisassociateDistributionWebACLRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the distribution that you're disassociating from the WAF web ACL.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DisassociateDistributionWebACLRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DisassociateDistributionWebACLRequest:
    out: DisassociateDistributionWebACLRequest = {}  # type: ignore[typeddict-item]
    return out
