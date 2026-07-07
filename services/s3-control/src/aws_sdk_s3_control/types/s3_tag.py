"""Generated from Smithy shape ``com.amazonaws.s3control#S3Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.tag_key_string
    import aws_sdk_s3_control.types.tag_value_string


class S3Tag(TypedDict, closed=True):
    key: "aws_sdk_s3_control.types.tag_key_string.TagKeyString"
    """<p>Key of the tag</p>"""
    value: "aws_sdk_s3_control.types.tag_value_string.TagValueString"
    """<p>Value of the tag</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Tag, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Key").text = str(value["key"])
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> S3Tag:
    out: S3Tag = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        raise DeserializationError("S3Tag.key required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("S3Tag.value required")
    return out
