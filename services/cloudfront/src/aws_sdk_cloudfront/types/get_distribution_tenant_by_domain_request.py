"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionTenantByDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetDistributionTenantByDomainRequest(TypedDict):
    domain: "aws_sdk_cloudfront.types.string.string"
    """<p>A domain name associated with the target distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetDistributionTenantByDomainRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetDistributionTenantByDomainRequest:
    out: GetDistributionTenantByDomainRequest = {}  # type: ignore[typeddict-item]
    return out
