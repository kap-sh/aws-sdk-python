"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteDistributionTenantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteDistributionTenantRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution tenant to delete.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The value of the <code>ETag</code> header that you received when retrieving the distribution tenant. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteDistributionTenantRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteDistributionTenantRequest:
    out: DeleteDistributionTenantRequest = {}  # type: ignore[typeddict-item]
    return out
