"""Generated from Smithy shape ``com.amazonaws.route53#CidrCollectionChanges``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.cidr_collection_change

CidrCollectionChanges: TypeAlias = list[
    "aws_sdk_route_53.types.cidr_collection_change.CidrCollectionChange"
]


# --- restXml ser/de ---
def serialize_xml(value: CidrCollectionChanges, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.cidr_collection_change

        aws_sdk_route_53.types.cidr_collection_change.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> CidrCollectionChanges:
    import aws_sdk_route_53.types.cidr_collection_change

    out: CidrCollectionChanges = []
    for child in el.findall("member"):
        out.append(aws_sdk_route_53.types.cidr_collection_change.deserialize_xml(child))
    return out


def serialize_xml_flat(value: CidrCollectionChanges, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.cidr_collection_change

        aws_sdk_route_53.types.cidr_collection_change.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> CidrCollectionChanges:
    import aws_sdk_route_53.types.cidr_collection_change

    out: CidrCollectionChanges = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.cidr_collection_change.deserialize_xml(child))
    return out
