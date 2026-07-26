"""Generated from Smithy shape ``com.amazonaws.s3control#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.non_empty_max_length64_string
    import capo_s3_control.types.non_empty_max_length1024_string

Endpoints: TypeAlias = dict[
    "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String",
    "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String",
]


# --- restXml ser/de ---
def serialize_xml(input_to_serialize: Endpoints, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for key, value in input_to_serialize.items():
        entry = SubElement(el, "entry")
        SubElement(entry, "key").text = str(key)
        SubElement(entry, "value").text = str(value)


def deserialize_xml(el: Element) -> Endpoints:
    out: Endpoints = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out


def serialize_xml_flat(
    input_to_serialize: Endpoints, parent: Element, tag: str
) -> None:
    for key, value in input_to_serialize.items():
        entry = SubElement(parent, tag)
        SubElement(entry, "key").text = str(key)
        SubElement(entry, "value").text = str(value)


def deserialize_xml_flat(parent: Element, tag: str) -> Endpoints:
    out: Endpoints = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out
