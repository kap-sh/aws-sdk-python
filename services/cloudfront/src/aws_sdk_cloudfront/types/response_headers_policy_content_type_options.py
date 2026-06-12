"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyContentTypeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean


class ResponseHeadersPolicyContentTypeOptions(TypedDict):
    override: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides the <code>X-Content-Type-Options</code> HTTP response header received from the origin with the one specified in this response headers policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyContentTypeOptions, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Override").text = "true" if value["override"] else "false"


def deserialize_xml(el: Element) -> ResponseHeadersPolicyContentTypeOptions:
    out: ResponseHeadersPolicyContentTypeOptions = {}  # type: ignore[typeddict-item]
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyContentTypeOptions.override required"
        )
    return out
