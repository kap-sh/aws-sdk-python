"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyValueStoreAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_value_store_arn


class KeyValueStoreAssociation(TypedDict):
    key_value_store_arn: "aws_sdk_cloudfront.types.key_value_store_arn.KeyValueStoreARN"
    """<p>The Amazon Resource Name (ARN) of the key value store association.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyValueStoreAssociation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "KeyValueStoreARN").text = str(value["key_value_store_arn"])


def deserialize_xml(el: Element) -> KeyValueStoreAssociation:
    out: KeyValueStoreAssociation = {}  # type: ignore[typeddict-item]
    child_key_value_store_arn = el.find("KeyValueStoreARN")
    if child_key_value_store_arn is not None:
        out["key_value_store_arn"] = str(child_key_value_store_arn.text or "")
    else:
        raise DeserializationError(
            "KeyValueStoreAssociation.key_value_store_arn required"
        )
    return out
