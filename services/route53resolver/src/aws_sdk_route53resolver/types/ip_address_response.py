"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.ip
    import aws_sdk_route53resolver.types.ip_address_status
    import aws_sdk_route53resolver.types.ipv6
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rfc3339_time_string
    import aws_sdk_route53resolver.types.status_message
    import aws_sdk_route53resolver.types.subnet_id


class IpAddressResponse(TypedDict):
    ip_id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of one IP address.</p>"""
    subnet_id: NotRequired["aws_sdk_route53resolver.types.subnet_id.SubnetId"]
    """<p>The ID of one subnet.</p>"""
    ip: NotRequired["aws_sdk_route53resolver.types.ip.Ip"]
    """<p>One IPv4 address that the Resolver endpoint uses for DNS queries.</p>"""
    ipv6: NotRequired["aws_sdk_route53resolver.types.ipv6.Ipv6"]
    """<p> One IPv6 address that the Resolver endpoint uses for DNS queries. </p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.ip_address_status.IpAddressStatus"
    ]
    """<p>A status code that gives the current status of the request.</p>"""
    status_message: NotRequired[
        "aws_sdk_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>A message that provides additional information about the status of the request.</p>"""
    creation_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the IP address was created, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    modification_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the IP address was last modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressResponse) -> dict:
    out: dict = {}
    if "ip_id" in value:
        out["IpId"] = value["ip_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "ip" in value:
        out["Ip"] = value["ip"]
    if "ipv6" in value:
        out["Ipv6"] = value["ipv6"]
    if "status" in value:
        import aws_sdk_route53resolver.types.ip_address_status

        out["Status"] = (
            aws_sdk_route53resolver.types.ip_address_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpAddressResponse:
    out: IpAddressResponse = {}  # type: ignore[typeddict-item]
    if "IpId" in data:
        out["ip_id"] = data["IpId"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "Ip" in data:
        out["ip"] = data["Ip"]
    if "Ipv6" in data:
        out["ipv6"] = data["Ipv6"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.ip_address_status

        out["status"] = (
            aws_sdk_route53resolver.types.ip_address_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "ModificationTime" in data:
        out["modification_time"] = data["ModificationTime"]
    return out
