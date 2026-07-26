"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustStoreStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

TrustStoreStatus: TypeAlias = Literal[
    "pending",
    "active",
    "failed",
]


# --- restXml ser/de ---
def to_xml_text(value: TrustStoreStatus) -> str:
    return value


def from_xml_text(text: str) -> TrustStoreStatus:
    return cast(TrustStoreStatus, text)


def serialize_xml(value: TrustStoreStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TrustStoreStatus:
    return from_xml_text(el.text or "")
