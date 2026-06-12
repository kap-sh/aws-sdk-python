"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionTenantAssociationFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DistributionTenantAssociationFilter(TypedDict):
    distribution_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The distribution ID to filter by. You can find distribution tenants associated with a specific distribution.</p>"""
    connection_group_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The ID of the connection group to filter by. You can find distribution tenants associated with a specific connection group.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DistributionTenantAssociationFilter, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_id" in value:
        SubElement(el, "DistributionId").text = str(value["distribution_id"])
    if "connection_group_id" in value:
        SubElement(el, "ConnectionGroupId").text = str(value["connection_group_id"])


def deserialize_xml(el: Element) -> DistributionTenantAssociationFilter:
    out: DistributionTenantAssociationFilter = {}  # type: ignore[typeddict-item]
    child_distribution_id = el.find("DistributionId")
    if child_distribution_id is not None:
        out["distribution_id"] = str(child_distribution_id.text or "")
    child_connection_group_id = el.find("ConnectionGroupId")
    if child_connection_group_id is not None:
        out["connection_group_id"] = str(child_connection_group_id.text or "")
    return out
