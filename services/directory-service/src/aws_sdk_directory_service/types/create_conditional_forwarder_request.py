"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateConditionalForwarderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.dns_ip_addrs
    import aws_sdk_directory_service.types.dns_ipv6_addrs
    import aws_sdk_directory_service.types.remote_domain_name


class CreateConditionalForwarderRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The directory ID of the Amazon Web Services directory for which you are creating the conditional forwarder.</p>"""
    remote_domain_name: (
        "aws_sdk_directory_service.types.remote_domain_name.RemoteDomainName"
    )
    """<p>The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.</p>"""
    dns_ip_addrs: "aws_sdk_directory_service.types.dns_ip_addrs.DnsIpAddrs"
    """<p>The IP addresses of the remote DNS server associated with RemoteDomainName.</p>"""
    dns_ipv6_addrs: NotRequired[
        "aws_sdk_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>The IPv6 addresses of the remote DNS server associated with RemoteDomainName.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConditionalForwarderRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["RemoteDomainName"] = value["remote_domain_name"]
    import aws_sdk_directory_service.types.dns_ip_addrs

    out["DnsIpAddrs"] = (
        aws_sdk_directory_service.types.dns_ip_addrs.serialize_aws_json_1_1(
            value.get("dns_ip_addrs", [])
        )
    )
    if "dns_ipv6_addrs" in value:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["DnsIpv6Addrs"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["dns_ipv6_addrs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConditionalForwarderRequest:
    out: CreateConditionalForwarderRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "CreateConditionalForwarderRequest.directory_id required"
        )
    if "RemoteDomainName" in data:
        out["remote_domain_name"] = data["RemoteDomainName"]
    else:
        raise DeserializationError(
            "CreateConditionalForwarderRequest.remote_domain_name required"
        )
    if "DnsIpAddrs" in data:
        import aws_sdk_directory_service.types.dns_ip_addrs

        out["dns_ip_addrs"] = (
            aws_sdk_directory_service.types.dns_ip_addrs.deserialize_aws_json_1_1(
                data["DnsIpAddrs"]
            )
        )
    else:
        out["dns_ip_addrs"] = []
    if "DnsIpv6Addrs" in data:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["dns_ipv6_addrs"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["DnsIpv6Addrs"]
            )
        )
    return out
