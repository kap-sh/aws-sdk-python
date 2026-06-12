"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachePolicySummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cache_policy
    import aws_sdk_cloudfront.types.cache_policy_type


class CachePolicySummary(TypedDict):
    type: "aws_sdk_cloudfront.types.cache_policy_type.CachePolicyType"
    """<p>The type of cache policy, either <code>managed</code> (created by Amazon Web Services) or <code>custom</code> (created in this Amazon Web Services account).</p>"""
    cache_policy: "aws_sdk_cloudfront.types.cache_policy.CachePolicy"
    """<p>The cache policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CachePolicySummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.cache_policy_type

    aws_sdk_cloudfront.types.cache_policy_type.serialize_xml(value["type"], el, "Type")
    import aws_sdk_cloudfront.types.cache_policy

    aws_sdk_cloudfront.types.cache_policy.serialize_xml(
        value["cache_policy"], el, "CachePolicy"
    )


def deserialize_xml(el: Element) -> CachePolicySummary:
    out: CachePolicySummary = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_cloudfront.types.cache_policy_type

        out["type"] = aws_sdk_cloudfront.types.cache_policy_type.deserialize_xml(
            child_type
        )
    else:
        raise DeserializationError("CachePolicySummary.type required")
    child_cache_policy = el.find("CachePolicy")
    if child_cache_policy is not None:
        import aws_sdk_cloudfront.types.cache_policy

        out["cache_policy"] = aws_sdk_cloudfront.types.cache_policy.deserialize_xml(
            child_cache_policy
        )
    else:
        raise DeserializationError("CachePolicySummary.cache_policy required")
    return out
