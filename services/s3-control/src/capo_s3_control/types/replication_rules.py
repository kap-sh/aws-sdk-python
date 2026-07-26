"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationRules``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.replication_rule

ReplicationRules: TypeAlias = list[
    "capo_s3_control.types.replication_rule.ReplicationRule"
]


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRules, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.replication_rule

        capo_s3_control.types.replication_rule.serialize_xml(item, el, "Rule")


def deserialize_xml(el: Element) -> ReplicationRules:
    import capo_s3_control.types.replication_rule

    out: ReplicationRules = []
    for child in el.findall("Rule"):
        out.append(capo_s3_control.types.replication_rule.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ReplicationRules, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.replication_rule

        capo_s3_control.types.replication_rule.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ReplicationRules:
    import capo_s3_control.types.replication_rule

    out: ReplicationRules = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.replication_rule.deserialize_xml(child))
    return out
