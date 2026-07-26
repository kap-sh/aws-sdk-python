"""Generated from Smithy shape ``com.amazonaws.s3#RoutingRules``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.routing_rule

RoutingRules: TypeAlias = list["capo_s3.types.routing_rule.RoutingRule"]


# --- restXml ser/de ---
def serialize_xml(value: RoutingRules, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.routing_rule

        capo_s3.types.routing_rule.serialize_xml(item, el, "RoutingRule")


def deserialize_xml(el: Element) -> RoutingRules:
    import capo_s3.types.routing_rule

    out: RoutingRules = []
    for child in el.findall("RoutingRule"):
        out.append(capo_s3.types.routing_rule.deserialize_xml(child))
    return out


def serialize_xml_flat(value: RoutingRules, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3.types.routing_rule

        capo_s3.types.routing_rule.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> RoutingRules:
    import capo_s3.types.routing_rule

    out: RoutingRules = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.routing_rule.deserialize_xml(child))
    return out
