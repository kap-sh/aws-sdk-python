"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateAnycastIpListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.ip_address_type
    import aws_sdk_cloudfront.types.ipam_cidr_config_list
    import aws_sdk_cloudfront.types.string


class UpdateAnycastIpListRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the Anycast static IP list.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_cloudfront.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type for the Anycast static IP list. You can specify one of the following options:</p> <ul> <li> <p> <code>ipv4</code> only</p> </li> <li> <p> <code>ipv6</code> only</p> </li> <li> <p> <code>dualstack</code> - Allocate a list of both IPv4 and IPv6 addresses</p> </li> </ul>"""
    ipam_cidr_configs: NotRequired[
        "aws_sdk_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
    ]
    """<p>A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for updating the Anycast static IP list.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version (ETag value) of the Anycast static IP list that you are updating.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateAnycastIpListRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "ip_address_type" in value:
        import aws_sdk_cloudfront.types.ip_address_type

        aws_sdk_cloudfront.types.ip_address_type.serialize_xml(
            value["ip_address_type"], el, "IpAddressType"
        )
    if "ipam_cidr_configs" in value:
        import aws_sdk_cloudfront.types.ipam_cidr_config_list

        aws_sdk_cloudfront.types.ipam_cidr_config_list.serialize_xml(
            value["ipam_cidr_configs"], el, "IpamCidrConfigs"
        )


def deserialize_xml(el: Element) -> UpdateAnycastIpListRequest:
    out: UpdateAnycastIpListRequest = {}  # type: ignore[typeddict-item]
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import aws_sdk_cloudfront.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_cloudfront.types.ip_address_type.deserialize_xml(
                child_ip_address_type
            )
        )
    child_ipam_cidr_configs = el.find("IpamCidrConfigs")
    if child_ipam_cidr_configs is not None:
        import aws_sdk_cloudfront.types.ipam_cidr_config_list

        out["ipam_cidr_configs"] = (
            aws_sdk_cloudfront.types.ipam_cidr_config_list.deserialize_xml(
                child_ipam_cidr_configs
            )
        )
    return out
