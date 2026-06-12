"""Generated from Smithy shape ``com.amazonaws.route53#CidrBlockSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.cidr_block_summary

CidrBlockSummaries: TypeAlias = list[
    "aws_sdk_route_53.types.cidr_block_summary.CidrBlockSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: CidrBlockSummaries, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.cidr_block_summary

        aws_sdk_route_53.types.cidr_block_summary.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> CidrBlockSummaries:
    import aws_sdk_route_53.types.cidr_block_summary

    out: CidrBlockSummaries = []
    for child in el.findall("member"):
        out.append(aws_sdk_route_53.types.cidr_block_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: CidrBlockSummaries, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.cidr_block_summary

        aws_sdk_route_53.types.cidr_block_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> CidrBlockSummaries:
    import aws_sdk_route_53.types.cidr_block_summary

    out: CidrBlockSummaries = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.cidr_block_summary.deserialize_xml(child))
    return out
