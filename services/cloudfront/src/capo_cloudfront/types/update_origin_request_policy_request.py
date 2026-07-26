"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateOriginRequestPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_request_policy_config
    import capo_cloudfront.types.string


class UpdateOriginRequestPolicyRequest(TypedDict, closed=True):
    origin_request_policy_config: (
        "capo_cloudfront.types.origin_request_policy_config.OriginRequestPolicyConfig"
    )
    """<p>An origin request policy configuration.</p>"""
    id: "capo_cloudfront.types.string.string"
    """<p>The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior's <code>OriginRequestPolicyId</code> field in the response to <code>GetDistributionConfig</code>.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The version of the origin request policy that you are updating. The version is returned in the origin request policy's <code>ETag</code> field in the response to <code>GetOriginRequestPolicyConfig</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateOriginRequestPolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.origin_request_policy_config

    capo_cloudfront.types.origin_request_policy_config.serialize_xml(
        value["origin_request_policy_config"], el, "OriginRequestPolicyConfig"
    )


def deserialize_xml(el: Element) -> UpdateOriginRequestPolicyRequest:
    out: UpdateOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
    child_origin_request_policy_config = el.find("OriginRequestPolicyConfig")
    if child_origin_request_policy_config is not None:
        import capo_cloudfront.types.origin_request_policy_config

        out["origin_request_policy_config"] = (
            capo_cloudfront.types.origin_request_policy_config.deserialize_xml(
                child_origin_request_policy_config
            )
        )
    else:
        raise DeserializationError(
            "UpdateOriginRequestPolicyRequest.origin_request_policy_config required"
        )
    return out
