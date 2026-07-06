"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyAccessControlAllowOrigins``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.access_control_allow_origins_list
    import aws_sdk_cloudfront.types.integer


class ResponseHeadersPolicyAccessControlAllowOrigins(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of origins in the list.</p>"""
    items: "aws_sdk_cloudfront.types.access_control_allow_origins_list.AccessControlAllowOriginsList"
    """<p>The list of origins (domain names). You can specify <code>*</code> to allow all origins.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyAccessControlAllowOrigins, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import aws_sdk_cloudfront.types.access_control_allow_origins_list

    aws_sdk_cloudfront.types.access_control_allow_origins_list.serialize_xml(
        value["items"], el, "Items"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyAccessControlAllowOrigins:
    out: ResponseHeadersPolicyAccessControlAllowOrigins = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyAccessControlAllowOrigins.quantity required"
        )
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.access_control_allow_origins_list

        out["items"] = (
            aws_sdk_cloudfront.types.access_control_allow_origins_list.deserialize_xml(
                child_items
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyAccessControlAllowOrigins.items required"
        )
    return out
