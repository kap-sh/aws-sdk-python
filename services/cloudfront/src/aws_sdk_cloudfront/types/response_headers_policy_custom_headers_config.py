"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyCustomHeadersConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.response_headers_policy_custom_header_list


class ResponseHeadersPolicyCustomHeadersConfig(TypedDict):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of HTTP response headers in the list.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.response_headers_policy_custom_header_list.ResponseHeadersPolicyCustomHeaderList"
    ]
    """<p>The list of HTTP response headers and their values.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyCustomHeadersConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.response_headers_policy_custom_header_list

        aws_sdk_cloudfront.types.response_headers_policy_custom_header_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyCustomHeadersConfig:
    out: ResponseHeadersPolicyCustomHeadersConfig = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyCustomHeadersConfig.quantity required"
        )
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.response_headers_policy_custom_header_list

        out["items"] = (
            aws_sdk_cloudfront.types.response_headers_policy_custom_header_list.deserialize_xml(
                child_items
            )
        )
    return out
