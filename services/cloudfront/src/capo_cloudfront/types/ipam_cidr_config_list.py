"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpamCidrConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.ipam_cidr_config

IpamCidrConfigList: TypeAlias = list[
    "capo_cloudfront.types.ipam_cidr_config.IpamCidrConfig"
]


# --- restXml ser/de ---
def serialize_xml(value: IpamCidrConfigList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.ipam_cidr_config

        capo_cloudfront.types.ipam_cidr_config.serialize_xml(item, el, "IpamCidrConfig")


def deserialize_xml(el: Element) -> IpamCidrConfigList:
    import capo_cloudfront.types.ipam_cidr_config

    out: IpamCidrConfigList = []
    for child in el.findall("IpamCidrConfig"):
        out.append(capo_cloudfront.types.ipam_cidr_config.deserialize_xml(child))
    return out


def serialize_xml_flat(value: IpamCidrConfigList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.ipam_cidr_config

        capo_cloudfront.types.ipam_cidr_config.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> IpamCidrConfigList:
    import capo_cloudfront.types.ipam_cidr_config

    out: IpamCidrConfigList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.ipam_cidr_config.deserialize_xml(child))
    return out
