"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustedSigners``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.aws_account_number_list
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.integer


class TrustedSigners(TypedDict):
    enabled: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>This field is <code>true</code> if any of the Amazon Web Services accounts in the list are configured as trusted signers. If not, this field is <code>false</code>.</p>"""
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of Amazon Web Services accounts in the list.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.aws_account_number_list.AwsAccountNumberList"
    ]
    """<p>A list of Amazon Web Services account identifiers.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrustedSigners, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.aws_account_number_list

        aws_sdk_cloudfront.types.aws_account_number_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> TrustedSigners:
    out: TrustedSigners = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("TrustedSigners.enabled required")
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("TrustedSigners.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.aws_account_number_list

        out["items"] = aws_sdk_cloudfront.types.aws_account_number_list.deserialize_xml(
            child_items
        )
    return out
