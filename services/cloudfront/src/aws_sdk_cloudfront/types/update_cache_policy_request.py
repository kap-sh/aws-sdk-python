"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateCachePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cache_policy_config
    import aws_sdk_cloudfront.types.string


class UpdateCachePolicyRequest(TypedDict, closed=True):
    cache_policy_config: (
        "aws_sdk_cloudfront.types.cache_policy_config.CachePolicyConfig"
    )
    """<p>A cache policy configuration.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior's <code>CachePolicyId</code> field in the response to <code>GetDistributionConfig</code>.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version of the cache policy that you are updating. The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetCachePolicyConfig</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateCachePolicyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.cache_policy_config

    aws_sdk_cloudfront.types.cache_policy_config.serialize_xml(
        value["cache_policy_config"], el, "CachePolicyConfig"
    )


def deserialize_xml(el: Element) -> UpdateCachePolicyRequest:
    out: UpdateCachePolicyRequest = {}  # type: ignore[typeddict-item]
    child_cache_policy_config = el.find("CachePolicyConfig")
    if child_cache_policy_config is not None:
        import aws_sdk_cloudfront.types.cache_policy_config

        out["cache_policy_config"] = (
            aws_sdk_cloudfront.types.cache_policy_config.deserialize_xml(
                child_cache_policy_config
            )
        )
    else:
        raise DeserializationError(
            "UpdateCachePolicyRequest.cache_policy_config required"
        )
    return out
