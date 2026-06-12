"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.hosted_zone_summary

HostedZoneSummaries: TypeAlias = list[
    "aws_sdk_route_53.types.hosted_zone_summary.HostedZoneSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneSummaries, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.hosted_zone_summary

        aws_sdk_route_53.types.hosted_zone_summary.serialize_xml(
            item, el, "HostedZoneSummary"
        )


def deserialize_xml(el: Element) -> HostedZoneSummaries:
    import aws_sdk_route_53.types.hosted_zone_summary

    out: HostedZoneSummaries = []
    for child in el.findall("HostedZoneSummary"):
        out.append(aws_sdk_route_53.types.hosted_zone_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: HostedZoneSummaries, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.hosted_zone_summary

        aws_sdk_route_53.types.hosted_zone_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> HostedZoneSummaries:
    import aws_sdk_route_53.types.hosted_zone_summary

    out: HostedZoneSummaries = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.hosted_zone_summary.deserialize_xml(child))
    return out
