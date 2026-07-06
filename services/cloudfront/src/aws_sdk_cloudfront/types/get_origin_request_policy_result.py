"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginRequestPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_request_policy
    import aws_sdk_cloudfront.types.string


class GetOriginRequestPolicyResult(TypedDict, closed=True):
    origin_request_policy: NotRequired[
        "aws_sdk_cloudfront.types.origin_request_policy.OriginRequestPolicy"
    ]
    """<p>The origin request policy.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the origin request policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetOriginRequestPolicyResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_request_policy" in value:
        import aws_sdk_cloudfront.types.origin_request_policy

        aws_sdk_cloudfront.types.origin_request_policy.serialize_xml(
            value["origin_request_policy"], el, "OriginRequestPolicy"
        )


def deserialize_xml(el: Element) -> GetOriginRequestPolicyResult:
    out: GetOriginRequestPolicyResult = {}  # type: ignore[typeddict-item]
    child_origin_request_policy = el.find("OriginRequestPolicy")
    if child_origin_request_policy is not None:
        import aws_sdk_cloudfront.types.origin_request_policy

        out["origin_request_policy"] = (
            aws_sdk_cloudfront.types.origin_request_policy.deserialize_xml(
                child_origin_request_policy
            )
        )
    return out
