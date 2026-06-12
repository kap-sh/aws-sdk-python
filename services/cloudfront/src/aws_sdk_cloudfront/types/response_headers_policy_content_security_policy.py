"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyContentSecurityPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.string


class ResponseHeadersPolicyContentSecurityPolicy(TypedDict):
    override: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides the <code>Content-Security-Policy</code> HTTP response header received from the origin with the one specified in this response headers policy.</p>"""
    content_security_policy: "aws_sdk_cloudfront.types.string.string"
    """<p>The policy directives and their values that CloudFront includes as values for the <code>Content-Security-Policy</code> HTTP response header.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyContentSecurityPolicy, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Override").text = "true" if value["override"] else "false"
    SubElement(el, "ContentSecurityPolicy").text = str(value["content_security_policy"])


def deserialize_xml(el: Element) -> ResponseHeadersPolicyContentSecurityPolicy:
    out: ResponseHeadersPolicyContentSecurityPolicy = {}  # type: ignore[typeddict-item]
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyContentSecurityPolicy.override required"
        )
    child_content_security_policy = el.find("ContentSecurityPolicy")
    if child_content_security_policy is not None:
        out["content_security_policy"] = str(child_content_security_policy.text or "")
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyContentSecurityPolicy.content_security_policy required"
        )
    return out
