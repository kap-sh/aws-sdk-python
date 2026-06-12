"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionTenantByDomainResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_tenant
    import aws_sdk_cloudfront.types.string


class GetDistributionTenantByDomainResult(TypedDict):
    distribution_tenant: NotRequired[
        "aws_sdk_cloudfront.types.distribution_tenant.DistributionTenant"
    ]
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetDistributionTenantByDomainResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_tenant" in value:
        import aws_sdk_cloudfront.types.distribution_tenant

        aws_sdk_cloudfront.types.distribution_tenant.serialize_xml(
            value["distribution_tenant"], el, "DistributionTenant"
        )


def deserialize_xml(el: Element) -> GetDistributionTenantByDomainResult:
    out: GetDistributionTenantByDomainResult = {}  # type: ignore[typeddict-item]
    child_distribution_tenant = el.find("DistributionTenant")
    if child_distribution_tenant is not None:
        import aws_sdk_cloudfront.types.distribution_tenant

        out["distribution_tenant"] = (
            aws_sdk_cloudfront.types.distribution_tenant.deserialize_xml(
                child_distribution_tenant
            )
        )
    return out
