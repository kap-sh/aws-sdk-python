"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListCachePoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_policy_list


class ListCachePoliciesResult(TypedDict, closed=True):
    cache_policy_list: NotRequired[
        "capo_cloudfront.types.cache_policy_list.CachePolicyList"
    ]
    """<p>A list of cache policies.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListCachePoliciesResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cache_policy_list" in value:
        import capo_cloudfront.types.cache_policy_list

        capo_cloudfront.types.cache_policy_list.serialize_xml(
            value["cache_policy_list"], el, "CachePolicyList"
        )


def deserialize_xml(el: Element) -> ListCachePoliciesResult:
    out: ListCachePoliciesResult = {}  # type: ignore[typeddict-item]
    child_cache_policy_list = el.find("CachePolicyList")
    if child_cache_policy_list is not None:
        import capo_cloudfront.types.cache_policy_list

        out["cache_policy_list"] = (
            capo_cloudfront.types.cache_policy_list.deserialize_xml(
                child_cache_policy_list
            )
        )
    return out
