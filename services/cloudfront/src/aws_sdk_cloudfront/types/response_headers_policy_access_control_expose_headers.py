"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyAccessControlExposeHeaders``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.access_control_expose_headers_list
    import aws_sdk_cloudfront.types.integer


class ResponseHeadersPolicyAccessControlExposeHeaders(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of HTTP headers in the list.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.access_control_expose_headers_list.AccessControlExposeHeadersList"
    ]
    """<p>The list of HTTP headers. You can specify <code>*</code> to expose all headers.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyAccessControlExposeHeaders, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.access_control_expose_headers_list

        aws_sdk_cloudfront.types.access_control_expose_headers_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyAccessControlExposeHeaders:
    out: ResponseHeadersPolicyAccessControlExposeHeaders = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyAccessControlExposeHeaders.quantity required"
        )
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.access_control_expose_headers_list

        out["items"] = (
            aws_sdk_cloudfront.types.access_control_expose_headers_list.deserialize_xml(
                child_items
            )
        )
    return out
