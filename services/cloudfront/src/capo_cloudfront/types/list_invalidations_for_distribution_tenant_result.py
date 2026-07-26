"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListInvalidationsForDistributionTenantResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.invalidation_list


class ListInvalidationsForDistributionTenantResult(TypedDict, closed=True):
    invalidation_list: NotRequired[
        "capo_cloudfront.types.invalidation_list.InvalidationList"
    ]


# --- restXml ser/de ---
def serialize_xml(
    value: ListInvalidationsForDistributionTenantResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "invalidation_list" in value:
        import capo_cloudfront.types.invalidation_list

        capo_cloudfront.types.invalidation_list.serialize_xml(
            value["invalidation_list"], el, "InvalidationList"
        )


def deserialize_xml(el: Element) -> ListInvalidationsForDistributionTenantResult:
    out: ListInvalidationsForDistributionTenantResult = {}  # type: ignore[typeddict-item]
    child_invalidation_list = el.find("InvalidationList")
    if child_invalidation_list is not None:
        import capo_cloudfront.types.invalidation_list

        out["invalidation_list"] = (
            capo_cloudfront.types.invalidation_list.deserialize_xml(
                child_invalidation_list
            )
        )
    return out
