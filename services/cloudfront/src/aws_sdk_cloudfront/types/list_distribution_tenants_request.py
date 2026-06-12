"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionTenantsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_tenant_association_filter
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListDistributionTenantsRequest(TypedDict):
    association_filter: NotRequired[
        "aws_sdk_cloudfront.types.distribution_tenant_association_filter.DistributionTenantAssociationFilter"
    ]
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The marker for the next set of results.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of distribution tenants to return.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionTenantsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "association_filter" in value:
        import aws_sdk_cloudfront.types.distribution_tenant_association_filter

        aws_sdk_cloudfront.types.distribution_tenant_association_filter.serialize_xml(
            value["association_filter"], el, "AssociationFilter"
        )
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListDistributionTenantsRequest:
    out: ListDistributionTenantsRequest = {}  # type: ignore[typeddict-item]
    child_association_filter = el.find("AssociationFilter")
    if child_association_filter is not None:
        import aws_sdk_cloudfront.types.distribution_tenant_association_filter

        out["association_filter"] = (
            aws_sdk_cloudfront.types.distribution_tenant_association_filter.deserialize_xml(
                child_association_filter
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
