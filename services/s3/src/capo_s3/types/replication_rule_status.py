"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRuleStatus``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

ReplicationRuleStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: ReplicationRuleStatus) -> str:
    return value


def from_xml_text(text: str) -> ReplicationRuleStatus:
    return cast(ReplicationRuleStatus, text)


def serialize_xml(value: ReplicationRuleStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ReplicationRuleStatus:
    return from_xml_text(el.text or "")
