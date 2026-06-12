"""Generated from Smithy shape ``com.amazonaws.cloudfront#DnsConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.dns_configuration

DnsConfigurationList: TypeAlias = list[
    "aws_sdk_cloudfront.types.dns_configuration.DnsConfiguration"
]


# --- restXml ser/de ---
def serialize_xml(value: DnsConfigurationList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.dns_configuration

        aws_sdk_cloudfront.types.dns_configuration.serialize_xml(
            item, el, "DnsConfiguration"
        )


def deserialize_xml(el: Element) -> DnsConfigurationList:
    import aws_sdk_cloudfront.types.dns_configuration

    out: DnsConfigurationList = []
    for child in el.findall("DnsConfiguration"):
        out.append(aws_sdk_cloudfront.types.dns_configuration.deserialize_xml(child))
    return out


def serialize_xml_flat(value: DnsConfigurationList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.dns_configuration

        aws_sdk_cloudfront.types.dns_configuration.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> DnsConfigurationList:
    import aws_sdk_cloudfront.types.dns_configuration

    out: DnsConfigurationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.dns_configuration.deserialize_xml(child))
    return out
