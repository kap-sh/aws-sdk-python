"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRules``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.replication_rule

ReplicationRules: TypeAlias = list["capo_s3.types.replication_rule.ReplicationRule"]


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRules, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.replication_rule

        capo_s3.types.replication_rule.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ReplicationRules:
    import capo_s3.types.replication_rule

    out: ReplicationRules = []
    for child in el.findall("member"):
        out.append(capo_s3.types.replication_rule.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ReplicationRules, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.replication_rule

        capo_s3.types.replication_rule.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ReplicationRules:
    import capo_s3.types.replication_rule

    out: ReplicationRules = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.replication_rule.deserialize_xml(child))
    return out
