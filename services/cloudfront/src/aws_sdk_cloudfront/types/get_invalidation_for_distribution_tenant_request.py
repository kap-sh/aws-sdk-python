"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetInvalidationForDistributionTenantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetInvalidationForDistributionTenantRequest(TypedDict):
    distribution_tenant_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution tenant.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the invalidation to retrieve.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetInvalidationForDistributionTenantRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetInvalidationForDistributionTenantRequest:
    out: GetInvalidationForDistributionTenantRequest = {}  # type: ignore[typeddict-item]
    return out
