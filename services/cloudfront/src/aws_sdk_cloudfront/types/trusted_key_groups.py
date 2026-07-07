"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustedKeyGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.trusted_key_group_id_list


class TrustedKeyGroups(TypedDict, closed=True):
    enabled: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>This field is <code>true</code> if any of the key groups in the list have public keys that CloudFront can use to verify the signatures of signed URLs and signed cookies. If not, this field is <code>false</code>.</p>"""
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of key groups in the list.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.trusted_key_group_id_list.TrustedKeyGroupIdList"
    ]
    """<p>A list of key groups identifiers.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrustedKeyGroups, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.trusted_key_group_id_list

        aws_sdk_cloudfront.types.trusted_key_group_id_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> TrustedKeyGroups:
    out: TrustedKeyGroups = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("TrustedKeyGroups.enabled required")
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("TrustedKeyGroups.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.trusted_key_group_id_list

        out["items"] = (
            aws_sdk_cloudfront.types.trusted_key_group_id_list.deserialize_xml(
                child_items
            )
        )
    return out
