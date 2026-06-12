"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpamCidrConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.ipam_cidr_config

IpamCidrConfigList: TypeAlias = list[
    "aws_sdk_cloudfront.types.ipam_cidr_config.IpamCidrConfig"
]


# --- restXml ser/de ---
def serialize_xml(value: IpamCidrConfigList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.ipam_cidr_config

        aws_sdk_cloudfront.types.ipam_cidr_config.serialize_xml(
            item, el, "IpamCidrConfig"
        )


def deserialize_xml(el: Element) -> IpamCidrConfigList:
    import aws_sdk_cloudfront.types.ipam_cidr_config

    out: IpamCidrConfigList = []
    for child in el.findall("IpamCidrConfig"):
        out.append(aws_sdk_cloudfront.types.ipam_cidr_config.deserialize_xml(child))
    return out


def serialize_xml_flat(value: IpamCidrConfigList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.ipam_cidr_config

        aws_sdk_cloudfront.types.ipam_cidr_config.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> IpamCidrConfigList:
    import aws_sdk_cloudfront.types.ipam_cidr_config

    out: IpamCidrConfigList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.ipam_cidr_config.deserialize_xml(child))
    return out
