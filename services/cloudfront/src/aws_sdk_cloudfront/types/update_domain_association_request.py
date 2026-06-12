"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateDomainAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_resource_id
    import aws_sdk_cloudfront.types.string


class UpdateDomainAssociationRequest(TypedDict):
    domain: "aws_sdk_cloudfront.types.string.string"
    """<p>The domain to update.</p>"""
    target_resource: (
        "aws_sdk_cloudfront.types.distribution_resource_id.DistributionResourceId"
    )
    """<p>The target standard distribution or distribution tenant resource for the domain. You can specify either <code>DistributionId</code> or <code>DistributionTenantId</code>, but not both.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> identifier for the standard distribution or distribution tenant that will be associated with the domain.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateDomainAssociationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    import aws_sdk_cloudfront.types.distribution_resource_id

    aws_sdk_cloudfront.types.distribution_resource_id.serialize_xml(
        value["target_resource"], el, "TargetResource"
    )


def deserialize_xml(el: Element) -> UpdateDomainAssociationRequest:
    out: UpdateDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        raise DeserializationError("UpdateDomainAssociationRequest.domain required")
    child_target_resource = el.find("TargetResource")
    if child_target_resource is not None:
        import aws_sdk_cloudfront.types.distribution_resource_id

        out["target_resource"] = (
            aws_sdk_cloudfront.types.distribution_resource_id.deserialize_xml(
                child_target_resource
            )
        )
    else:
        raise DeserializationError(
            "UpdateDomainAssociationRequest.target_resource required"
        )
    return out
