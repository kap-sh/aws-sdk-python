"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetResponseHeadersPolicyConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.response_headers_policy_config
    import aws_sdk_cloudfront.types.string


class GetResponseHeadersPolicyConfigResult(TypedDict, closed=True):
    response_headers_policy_config: NotRequired[
        "aws_sdk_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig"
    ]
    """<p>Contains a response headers policy.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the response headers policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetResponseHeadersPolicyConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "response_headers_policy_config" in value:
        import aws_sdk_cloudfront.types.response_headers_policy_config

        aws_sdk_cloudfront.types.response_headers_policy_config.serialize_xml(
            value["response_headers_policy_config"], el, "ResponseHeadersPolicyConfig"
        )


def deserialize_xml(el: Element) -> GetResponseHeadersPolicyConfigResult:
    out: GetResponseHeadersPolicyConfigResult = {}  # type: ignore[typeddict-item]
    child_response_headers_policy_config = el.find("ResponseHeadersPolicyConfig")
    if child_response_headers_policy_config is not None:
        import aws_sdk_cloudfront.types.response_headers_policy_config

        out["response_headers_policy_config"] = (
            aws_sdk_cloudfront.types.response_headers_policy_config.deserialize_xml(
                child_response_headers_policy_config
            )
        )
    return out
