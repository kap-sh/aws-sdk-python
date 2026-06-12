"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateAnycastIpListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.anycast_ip_list_name
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.ip_address_type
    import aws_sdk_cloudfront.types.ipam_cidr_config_list
    import aws_sdk_cloudfront.types.tags


class CreateAnycastIpListRequest(TypedDict):
    name: "aws_sdk_cloudfront.types.anycast_ip_list_name.AnycastIpListName"
    """<p>Name of the Anycast static IP list.</p>"""
    ip_count: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of static IP addresses that are allocated to the Anycast static IP list. Valid values: 21 or 3.</p>"""
    tags: NotRequired["aws_sdk_cloudfront.types.tags.Tags"]
    ip_address_type: NotRequired[
        "aws_sdk_cloudfront.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type for the Anycast static IP list. You can specify one of the following options:</p> <ul> <li> <p> <code>ipv4</code> only</p> </li> <li> <p> <code>ipv6</code> only </p> </li> <li> <p> <code>dualstack</code> - Allocate a list of both IPv4 and IPv6 addresses</p> </li> </ul>"""
    ipam_cidr_configs: NotRequired[
        "aws_sdk_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
    ]
    """<p> A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for creating the Anycast static IP list. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateAnycastIpListRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "IpCount").text = str(value["ip_count"])
    if "tags" in value:
        import aws_sdk_cloudfront.types.tags

        aws_sdk_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")
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


def deserialize_xml(el: Element) -> CreateAnycastIpListRequest:
    out: CreateAnycastIpListRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateAnycastIpListRequest.name required")
    child_ip_count = el.find("IpCount")
    if child_ip_count is not None:
        out["ip_count"] = int(child_ip_count.text or "")
    else:
        raise DeserializationError("CreateAnycastIpListRequest.ip_count required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudfront.types.tags

        out["tags"] = aws_sdk_cloudfront.types.tags.deserialize_xml(child_tags)
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
