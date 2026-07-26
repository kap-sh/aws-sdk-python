"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateCachePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_policy
    import capo_cloudfront.types.string


class UpdateCachePolicyResult(TypedDict, closed=True):
    cache_policy: NotRequired["capo_cloudfront.types.cache_policy.CachePolicy"]
    """<p>A cache policy.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the cache policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateCachePolicyResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cache_policy" in value:
        import capo_cloudfront.types.cache_policy

        capo_cloudfront.types.cache_policy.serialize_xml(
            value["cache_policy"], el, "CachePolicy"
        )


def deserialize_xml(el: Element) -> UpdateCachePolicyResult:
    out: UpdateCachePolicyResult = {}  # type: ignore[typeddict-item]
    child_cache_policy = el.find("CachePolicy")
    if child_cache_policy is not None:
        import capo_cloudfront.types.cache_policy

        out["cache_policy"] = capo_cloudfront.types.cache_policy.deserialize_xml(
            child_cache_policy
        )
    return out
