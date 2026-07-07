"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyCustomHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.string


class ResponseHeadersPolicyCustomHeader(TypedDict, closed=True):
    header: "aws_sdk_cloudfront.types.string.string"
    """<p>The HTTP response header name.</p>"""
    value: "aws_sdk_cloudfront.types.string.string"
    """<p>The value for the HTTP response header.</p>"""
    override: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides a response header with the same name received from the origin with the header specified here.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyCustomHeader, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Header").text = str(value["header"])
    SubElement(el, "Value").text = str(value["value"])
    SubElement(el, "Override").text = "true" if value["override"] else "false"


def deserialize_xml(el: Element) -> ResponseHeadersPolicyCustomHeader:
    out: ResponseHeadersPolicyCustomHeader = {}  # type: ignore[typeddict-item]
    child_header = el.find("Header")
    if child_header is not None:
        out["header"] = str(child_header.text or "")
    else:
        raise DeserializationError("ResponseHeadersPolicyCustomHeader.header required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("ResponseHeadersPolicyCustomHeader.value required")
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyCustomHeader.override required"
        )
    return out
