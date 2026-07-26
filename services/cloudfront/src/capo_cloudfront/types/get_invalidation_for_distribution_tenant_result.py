"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetInvalidationForDistributionTenantResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.invalidation


class GetInvalidationForDistributionTenantResult(TypedDict, closed=True):
    invalidation: NotRequired["capo_cloudfront.types.invalidation.Invalidation"]


# --- restXml ser/de ---
def serialize_xml(
    value: GetInvalidationForDistributionTenantResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "invalidation" in value:
        import capo_cloudfront.types.invalidation

        capo_cloudfront.types.invalidation.serialize_xml(
            value["invalidation"], el, "Invalidation"
        )


def deserialize_xml(el: Element) -> GetInvalidationForDistributionTenantResult:
    out: GetInvalidationForDistributionTenantResult = {}  # type: ignore[typeddict-item]
    child_invalidation = el.find("Invalidation")
    if child_invalidation is not None:
        import capo_cloudfront.types.invalidation

        out["invalidation"] = capo_cloudfront.types.invalidation.deserialize_xml(
            child_invalidation
        )
    return out
