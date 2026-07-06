"""Generated from Smithy shape ``com.amazonaws.cloudfront#StatusCodes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.status_code_list


class StatusCodes(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of status codes.</p>"""
    items: "aws_sdk_cloudfront.types.status_code_list.StatusCodeList"
    """<p>The items (status codes) for an origin group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StatusCodes, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import aws_sdk_cloudfront.types.status_code_list

    aws_sdk_cloudfront.types.status_code_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> StatusCodes:
    out: StatusCodes = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("StatusCodes.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.status_code_list

        out["items"] = aws_sdk_cloudfront.types.status_code_list.deserialize_xml(
            child_items
        )
    else:
        raise DeserializationError("StatusCodes.items required")
    return out
