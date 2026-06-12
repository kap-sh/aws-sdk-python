"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetCachePolicyConfigResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cache_policy_config
    import aws_sdk_cloudfront.types.string


class GetCachePolicyConfigResult(TypedDict):
    cache_policy_config: NotRequired[
        "aws_sdk_cloudfront.types.cache_policy_config.CachePolicyConfig"
    ]
    """<p>The cache policy configuration.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the cache policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetCachePolicyConfigResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cache_policy_config" in value:
        import aws_sdk_cloudfront.types.cache_policy_config

        aws_sdk_cloudfront.types.cache_policy_config.serialize_xml(
            value["cache_policy_config"], el, "CachePolicyConfig"
        )


def deserialize_xml(el: Element) -> GetCachePolicyConfigResult:
    out: GetCachePolicyConfigResult = {}  # type: ignore[typeddict-item]
    child_cache_policy_config = el.find("CachePolicyConfig")
    if child_cache_policy_config is not None:
        import aws_sdk_cloudfront.types.cache_policy_config

        out["cache_policy_config"] = (
            aws_sdk_cloudfront.types.cache_policy_config.deserialize_xml(
                child_cache_policy_config
            )
        )
    return out
