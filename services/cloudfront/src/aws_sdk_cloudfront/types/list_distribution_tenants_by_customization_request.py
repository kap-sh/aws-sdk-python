"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionTenantsByCustomizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListDistributionTenantsByCustomizationRequest(TypedDict):
    web_acl_arn: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Filter by the ARN of the associated WAF web ACL.</p>"""
    certificate_arn: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Filter by the ARN of the associated ACM certificate.</p>"""
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The marker for the next set of results.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of distribution tenants to return by the specified customization.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionTenantsByCustomizationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "web_acl_arn" in value:
        SubElement(el, "WebACLArn").text = str(value["web_acl_arn"])
    if "certificate_arn" in value:
        SubElement(el, "CertificateArn").text = str(value["certificate_arn"])
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListDistributionTenantsByCustomizationRequest:
    out: ListDistributionTenantsByCustomizationRequest = {}  # type: ignore[typeddict-item]
    child_web_acl_arn = el.find("WebACLArn")
    if child_web_acl_arn is not None:
        out["web_acl_arn"] = str(child_web_acl_arn.text or "")
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
