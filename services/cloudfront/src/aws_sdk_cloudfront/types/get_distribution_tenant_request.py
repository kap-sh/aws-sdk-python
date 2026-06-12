"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionTenantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetDistributionTenantRequest(TypedDict):
    identifier: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetDistributionTenantRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetDistributionTenantRequest:
    out: GetDistributionTenantRequest = {}  # type: ignore[typeddict-item]
    return out
