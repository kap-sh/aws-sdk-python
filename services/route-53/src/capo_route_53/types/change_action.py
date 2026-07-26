"""Generated from Smithy shape ``com.amazonaws.route53#ChangeAction``."""

from typing import Literal, TypeAlias, cast

from capo_route_53._protocol.xml import Element, SubElement

ChangeAction: TypeAlias = Literal[
    "CREATE",
    "DELETE",
    "UPSERT",
]


# --- restXml ser/de ---
def to_xml_text(value: ChangeAction) -> str:
    return value


def from_xml_text(text: str) -> ChangeAction:
    return cast(ChangeAction, text)


def serialize_xml(value: ChangeAction, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChangeAction:
    return from_xml_text(el.text or "")
