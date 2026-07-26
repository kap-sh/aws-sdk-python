"""Generated from Smithy shape ``com.amazonaws.s3#Metadata``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.metadata_key
    import capo_s3.types.metadata_value

Metadata: TypeAlias = dict[
    "capo_s3.types.metadata_key.MetadataKey",
    "capo_s3.types.metadata_value.MetadataValue",
]


# --- restXml ser/de ---
def serialize_xml(input_to_serialize: Metadata, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for key, value in input_to_serialize.items():
        entry = SubElement(el, "entry")
        SubElement(entry, "key").text = str(key)
        SubElement(entry, "value").text = str(value)


def deserialize_xml(el: Element) -> Metadata:
    out: Metadata = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out


def serialize_xml_flat(input_to_serialize: Metadata, parent: Element, tag: str) -> None:
    for key, value in input_to_serialize.items():
        entry = SubElement(parent, tag)
        SubElement(entry, "key").text = str(key)
        SubElement(entry, "value").text = str(value)


def deserialize_xml_flat(parent: Element, tag: str) -> Metadata:
    out: Metadata = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out
