"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateResponseHeadersPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.response_headers_policy_config
    import aws_sdk_cloudfront.types.string


class UpdateResponseHeadersPolicyRequest(TypedDict, closed=True):
    response_headers_policy_config: "aws_sdk_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig"
    """<p>A response headers policy configuration.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier for the response headers policy that you are updating.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version of the response headers policy that you are updating.</p> <p>The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetResponseHeadersPolicyConfig</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateResponseHeadersPolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.response_headers_policy_config

    aws_sdk_cloudfront.types.response_headers_policy_config.serialize_xml(
        value["response_headers_policy_config"], el, "ResponseHeadersPolicyConfig"
    )


def deserialize_xml(el: Element) -> UpdateResponseHeadersPolicyRequest:
    out: UpdateResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
    child_response_headers_policy_config = el.find("ResponseHeadersPolicyConfig")
    if child_response_headers_policy_config is not None:
        import aws_sdk_cloudfront.types.response_headers_policy_config

        out["response_headers_policy_config"] = (
            aws_sdk_cloudfront.types.response_headers_policy_config.deserialize_xml(
                child_response_headers_policy_config
            )
        )
    else:
        raise DeserializationError(
            "UpdateResponseHeadersPolicyRequest.response_headers_policy_config required"
        )
    return out
