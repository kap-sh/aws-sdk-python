"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateCachePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_policy_config


class CreateCachePolicyRequest(TypedDict, closed=True):
    cache_policy_config: "capo_cloudfront.types.cache_policy_config.CachePolicyConfig"
    """<p>A cache policy configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateCachePolicyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.cache_policy_config

    capo_cloudfront.types.cache_policy_config.serialize_xml(
        value["cache_policy_config"], el, "CachePolicyConfig"
    )


def deserialize_xml(el: Element) -> CreateCachePolicyRequest:
    out: CreateCachePolicyRequest = {}  # type: ignore[typeddict-item]
    child_cache_policy_config = el.find("CachePolicyConfig")
    if child_cache_policy_config is not None:
        import capo_cloudfront.types.cache_policy_config

        out["cache_policy_config"] = (
            capo_cloudfront.types.cache_policy_config.deserialize_xml(
                child_cache_policy_config
            )
        )
    else:
        raise DeserializationError(
            "CreateCachePolicyRequest.cache_policy_config required"
        )
    return out
