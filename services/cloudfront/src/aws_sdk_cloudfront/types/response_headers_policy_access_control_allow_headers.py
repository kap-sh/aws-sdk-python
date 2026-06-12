"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyAccessControlAllowHeaders``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.access_control_allow_headers_list
    import aws_sdk_cloudfront.types.integer


class ResponseHeadersPolicyAccessControlAllowHeaders(TypedDict):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of HTTP header names in the list.</p>"""
    items: "aws_sdk_cloudfront.types.access_control_allow_headers_list.AccessControlAllowHeadersList"
    """<p>The list of HTTP header names. You can specify <code>*</code> to allow all headers.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyAccessControlAllowHeaders, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import aws_sdk_cloudfront.types.access_control_allow_headers_list

    aws_sdk_cloudfront.types.access_control_allow_headers_list.serialize_xml(
        value["items"], el, "Items"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyAccessControlAllowHeaders:
    out: ResponseHeadersPolicyAccessControlAllowHeaders = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyAccessControlAllowHeaders.quantity required"
        )
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.access_control_allow_headers_list

        out["items"] = (
            aws_sdk_cloudfront.types.access_control_allow_headers_list.deserialize_xml(
                child_items
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyAccessControlAllowHeaders.items required"
        )
    return out
