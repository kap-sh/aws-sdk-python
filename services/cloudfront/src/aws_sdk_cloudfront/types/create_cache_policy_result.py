"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateCachePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cache_policy
    import aws_sdk_cloudfront.types.string


class CreateCachePolicyResult(TypedDict, closed=True):
    cache_policy: NotRequired["aws_sdk_cloudfront.types.cache_policy.CachePolicy"]
    """<p>A cache policy.</p>"""
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The fully qualified URI of the cache policy just created.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the cache policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateCachePolicyResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cache_policy" in value:
        import aws_sdk_cloudfront.types.cache_policy

        aws_sdk_cloudfront.types.cache_policy.serialize_xml(
            value["cache_policy"], el, "CachePolicy"
        )


def deserialize_xml(el: Element) -> CreateCachePolicyResult:
    out: CreateCachePolicyResult = {}  # type: ignore[typeddict-item]
    child_cache_policy = el.find("CachePolicy")
    if child_cache_policy is not None:
        import aws_sdk_cloudfront.types.cache_policy

        out["cache_policy"] = aws_sdk_cloudfront.types.cache_policy.deserialize_xml(
            child_cache_policy
        )
    return out
