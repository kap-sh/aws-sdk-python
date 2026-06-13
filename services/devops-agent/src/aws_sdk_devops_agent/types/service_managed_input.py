"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceManagedInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.certificate_string
    import aws_sdk_devops_agent.types.ip_address_or_dns_name
    import aws_sdk_devops_agent.types.ip_address_type
    import aws_sdk_devops_agent.types.list_of_security_group_ids
    import aws_sdk_devops_agent.types.list_of_subnet_ids
    import aws_sdk_devops_agent.types.max_ipv4_addresses_per_eni
    import aws_sdk_devops_agent.types.port_ranges
    import aws_sdk_devops_agent.types.resource_config_dns_resolution
    import aws_sdk_devops_agent.types.vpc_id


class ServiceManagedInput(TypedDict):
    host_address: "aws_sdk_devops_agent.types.ip_address_or_dns_name.IpAddressOrDnsName"
    """<p>IP address or DNS name of the target resource.</p>"""
    vpc_id: "aws_sdk_devops_agent.types.vpc_id.VpcId"
    """<p>VPC to create the service-managed Resource Gateway in.</p>"""
    subnet_ids: "aws_sdk_devops_agent.types.list_of_subnet_ids.ListOfSubnetIds"
    """<p>Subnets that the service-managed Resource Gateway will span.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_devops_agent.types.list_of_security_group_ids.ListOfSecurityGroupIds"
    ]
    """<p>Security groups to attach to the service-managed Resource Gateway. If not specified, a default security group is created.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_devops_agent.types.ip_address_type.IpAddressType"
    ]
    """<p>IP address type of the service-managed Resource Gateway.</p>"""
    ipv4_addresses_per_eni: NotRequired[
        "aws_sdk_devops_agent.types.max_ipv4_addresses_per_eni.MaxIpv4AddressesPerEni"
    ]
    """<p>Number of IPv4 addresses in each ENI for the service-managed Resource Gateway.</p>"""
    port_ranges: NotRequired["aws_sdk_devops_agent.types.port_ranges.PortRanges"]
    """<p>TCP port ranges that a consumer can use to access the resource.</p>"""
    certificate: NotRequired[
        "aws_sdk_devops_agent.types.certificate_string.CertificateString"
    ]
    """<p>Certificate for the Private Connection.</p>"""
    dns_resolution: NotRequired[
        "aws_sdk_devops_agent.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>DNS resolution mode for the resource gateway. Defaults to PUBLIC when not set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedInput) -> dict:
    out: dict = {}
    out["hostAddress"] = value["host_address"]
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_devops_agent.types.list_of_subnet_ids

    out["subnetIds"] = aws_sdk_devops_agent.types.list_of_subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    if "security_group_ids" in value:
        import aws_sdk_devops_agent.types.list_of_security_group_ids

        out["securityGroupIds"] = (
            aws_sdk_devops_agent.types.list_of_security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        import aws_sdk_devops_agent.types.ip_address_type

        out["ipAddressType"] = (
            aws_sdk_devops_agent.types.ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    if "ipv4_addresses_per_eni" in value:
        out["ipv4AddressesPerEni"] = value["ipv4_addresses_per_eni"]
    if "port_ranges" in value:
        import aws_sdk_devops_agent.types.port_ranges

        out["portRanges"] = aws_sdk_devops_agent.types.port_ranges.serialize_json(
            value["port_ranges"]
        )
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    if "dns_resolution" in value:
        import aws_sdk_devops_agent.types.resource_config_dns_resolution

        out["dnsResolution"] = (
            aws_sdk_devops_agent.types.resource_config_dns_resolution.serialize_json(
                value["dns_resolution"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceManagedInput:
    out: ServiceManagedInput = {}  # type: ignore[typeddict-item]
    if "hostAddress" in data:
        out["host_address"] = data["hostAddress"]
    else:
        raise DeserializationError("ServiceManagedInput.host_address required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("ServiceManagedInput.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_devops_agent.types.list_of_subnet_ids

        out["subnet_ids"] = (
            aws_sdk_devops_agent.types.list_of_subnet_ids.deserialize_json(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("ServiceManagedInput.subnet_ids required")
    if "securityGroupIds" in data:
        import aws_sdk_devops_agent.types.list_of_security_group_ids

        out["security_group_ids"] = (
            aws_sdk_devops_agent.types.list_of_security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "ipAddressType" in data:
        import aws_sdk_devops_agent.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_devops_agent.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if "ipv4AddressesPerEni" in data:
        out["ipv4_addresses_per_eni"] = data["ipv4AddressesPerEni"]
    if "portRanges" in data:
        import aws_sdk_devops_agent.types.port_ranges

        out["port_ranges"] = aws_sdk_devops_agent.types.port_ranges.deserialize_json(
            data["portRanges"]
        )
    if "certificate" in data:
        out["certificate"] = data["certificate"]
    if "dnsResolution" in data:
        import aws_sdk_devops_agent.types.resource_config_dns_resolution

        out["dns_resolution"] = (
            aws_sdk_devops_agent.types.resource_config_dns_resolution.deserialize_json(
                data["dnsResolution"]
            )
        )
    return out
