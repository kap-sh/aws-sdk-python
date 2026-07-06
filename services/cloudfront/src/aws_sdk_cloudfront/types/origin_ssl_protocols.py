"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginSslProtocols``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.ssl_protocols_list


class OriginSslProtocols(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.</p>"""
    items: "aws_sdk_cloudfront.types.ssl_protocols_list.SslProtocolsList"
    """<p>A list that contains allowed SSL/TLS protocols for this distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginSslProtocols, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import aws_sdk_cloudfront.types.ssl_protocols_list

    aws_sdk_cloudfront.types.ssl_protocols_list.serialize_xml(
        value["items"], el, "Items"
    )


def deserialize_xml(el: Element) -> OriginSslProtocols:
    out: OriginSslProtocols = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("OriginSslProtocols.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.ssl_protocols_list

        out["items"] = aws_sdk_cloudfront.types.ssl_protocols_list.deserialize_xml(
            child_items
        )
    else:
        raise DeserializationError("OriginSslProtocols.items required")
    return out
