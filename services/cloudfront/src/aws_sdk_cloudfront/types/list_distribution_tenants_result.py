"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionTenantsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_tenant_list
    import aws_sdk_cloudfront.types.string


class ListDistributionTenantsResult(TypedDict):
    next_marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.</p>"""
    distribution_tenant_list: NotRequired[
        "aws_sdk_cloudfront.types.distribution_tenant_list.DistributionTenantList"
    ]
    """<p>The list of distribution tenants that you retrieved.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionTenantsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    if "distribution_tenant_list" in value:
        import aws_sdk_cloudfront.types.distribution_tenant_list

        aws_sdk_cloudfront.types.distribution_tenant_list.serialize_xml(
            value["distribution_tenant_list"], el, "DistributionTenantList"
        )


def deserialize_xml(el: Element) -> ListDistributionTenantsResult:
    out: ListDistributionTenantsResult = {}  # type: ignore[typeddict-item]
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_distribution_tenant_list = el.find("DistributionTenantList")
    if child_distribution_tenant_list is not None:
        import aws_sdk_cloudfront.types.distribution_tenant_list

        out["distribution_tenant_list"] = (
            aws_sdk_cloudfront.types.distribution_tenant_list.deserialize_xml(
                child_distribution_tenant_list
            )
        )
    return out
