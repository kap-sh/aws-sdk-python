"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListOriginRequestPoliciesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_request_policy_list


class ListOriginRequestPoliciesResult(TypedDict):
    origin_request_policy_list: NotRequired[
        "aws_sdk_cloudfront.types.origin_request_policy_list.OriginRequestPolicyList"
    ]
    """<p>A list of origin request policies.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListOriginRequestPoliciesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_request_policy_list" in value:
        import aws_sdk_cloudfront.types.origin_request_policy_list

        aws_sdk_cloudfront.types.origin_request_policy_list.serialize_xml(
            value["origin_request_policy_list"], el, "OriginRequestPolicyList"
        )


def deserialize_xml(el: Element) -> ListOriginRequestPoliciesResult:
    out: ListOriginRequestPoliciesResult = {}  # type: ignore[typeddict-item]
    child_origin_request_policy_list = el.find("OriginRequestPolicyList")
    if child_origin_request_policy_list is not None:
        import aws_sdk_cloudfront.types.origin_request_policy_list

        out["origin_request_policy_list"] = (
            aws_sdk_cloudfront.types.origin_request_policy_list.deserialize_xml(
                child_origin_request_policy_list
            )
        )
    return out
