"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListOriginRequestPoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_request_policy_list


class ListOriginRequestPoliciesResult(TypedDict, closed=True):
    origin_request_policy_list: NotRequired[
        "capo_cloudfront.types.origin_request_policy_list.OriginRequestPolicyList"
    ]
    """<p>A list of origin request policies.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListOriginRequestPoliciesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_request_policy_list" in value:
        import capo_cloudfront.types.origin_request_policy_list

        capo_cloudfront.types.origin_request_policy_list.serialize_xml(
            value["origin_request_policy_list"], el, "OriginRequestPolicyList"
        )


def deserialize_xml(el: Element) -> ListOriginRequestPoliciesResult:
    out: ListOriginRequestPoliciesResult = {}  # type: ignore[typeddict-item]
    child_origin_request_policy_list = el.find("OriginRequestPolicyList")
    if child_origin_request_policy_list is not None:
        import capo_cloudfront.types.origin_request_policy_list

        out["origin_request_policy_list"] = (
            capo_cloudfront.types.origin_request_policy_list.deserialize_xml(
                child_origin_request_policy_list
            )
        )
    return out
