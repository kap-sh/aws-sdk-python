"""Generated from Smithy shape ``com.amazonaws.cloudfront#CustomHeaders``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.origin_custom_headers_list


class CustomHeaders(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of custom headers, if any, for this distribution.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.origin_custom_headers_list.OriginCustomHeadersList"
    ]
    """<p> <b>Optional</b>: A list that contains one <code>OriginCustomHeader</code> element for each custom header that you want CloudFront to forward to the origin. If Quantity is <code>0</code>, omit <code>Items</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CustomHeaders, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.origin_custom_headers_list

        aws_sdk_cloudfront.types.origin_custom_headers_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> CustomHeaders:
    out: CustomHeaders = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("CustomHeaders.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.origin_custom_headers_list

        out["items"] = (
            aws_sdk_cloudfront.types.origin_custom_headers_list.deserialize_xml(
                child_items
            )
        )
    return out
