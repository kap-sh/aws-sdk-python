"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListResponseHeadersPoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.response_headers_policy_list


class ListResponseHeadersPoliciesResult(TypedDict, closed=True):
    response_headers_policy_list: NotRequired[
        "aws_sdk_cloudfront.types.response_headers_policy_list.ResponseHeadersPolicyList"
    ]
    """<p>A list of response headers policies.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListResponseHeadersPoliciesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "response_headers_policy_list" in value:
        import aws_sdk_cloudfront.types.response_headers_policy_list

        aws_sdk_cloudfront.types.response_headers_policy_list.serialize_xml(
            value["response_headers_policy_list"], el, "ResponseHeadersPolicyList"
        )


def deserialize_xml(el: Element) -> ListResponseHeadersPoliciesResult:
    out: ListResponseHeadersPoliciesResult = {}  # type: ignore[typeddict-item]
    child_response_headers_policy_list = el.find("ResponseHeadersPolicyList")
    if child_response_headers_policy_list is not None:
        import aws_sdk_cloudfront.types.response_headers_policy_list

        out["response_headers_policy_list"] = (
            aws_sdk_cloudfront.types.response_headers_policy_list.deserialize_xml(
                child_response_headers_policy_list
            )
        )
    return out
