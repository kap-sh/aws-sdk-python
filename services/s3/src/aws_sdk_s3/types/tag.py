"""Generated from Smithy shape ``com.amazonaws.s3#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_key
    import aws_sdk_s3.types.value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_s3.types.object_key.ObjectKey"
    """<p>Name of the object key.</p>"""
    value: "aws_sdk_s3.types.value.Value"
    """<p>Value of the tag.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Tag, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Key").text = str(value["key"])
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        raise DeserializationError("Tag.key required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("Tag.value required")
    return out
