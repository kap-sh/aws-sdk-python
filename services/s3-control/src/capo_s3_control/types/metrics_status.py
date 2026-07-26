"""Generated from Smithy shape ``com.amazonaws.s3control#MetricsStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

MetricsStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: MetricsStatus) -> str:
    return value


def from_xml_text(text: str) -> MetricsStatus:
    return cast(MetricsStatus, text)


def serialize_xml(value: MetricsStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MetricsStatus:
    return from_xml_text(el.text or "")
