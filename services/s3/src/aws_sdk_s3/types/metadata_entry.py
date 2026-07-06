"""Generated from Smithy shape ``com.amazonaws.s3#MetadataEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.metadata_key
    import aws_sdk_s3.types.metadata_value


class MetadataEntry(TypedDict, closed=True):
    name: NotRequired["aws_sdk_s3.types.metadata_key.MetadataKey"]
    """<p>Name of the object.</p>"""
    value: NotRequired["aws_sdk_s3.types.metadata_value.MetadataValue"]
    """<p>Value of the object.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: MetadataEntry, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "value" in value:
        SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> MetadataEntry:
    out: MetadataEntry = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
