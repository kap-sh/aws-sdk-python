"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateTrustRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.dns_ip_addrs
    import aws_sdk_directory_service.types.dns_ipv6_addrs
    import aws_sdk_directory_service.types.remote_domain_name
    import aws_sdk_directory_service.types.selective_auth
    import aws_sdk_directory_service.types.trust_direction
    import aws_sdk_directory_service.types.trust_password
    import aws_sdk_directory_service.types.trust_type


class CreateTrustRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The Directory ID of the Managed Microsoft AD directory for which to establish the trust relationship.</p>"""
    remote_domain_name: (
        "aws_sdk_directory_service.types.remote_domain_name.RemoteDomainName"
    )
    """<p>The Fully Qualified Domain Name (FQDN) of the external domain for which to create the trust relationship.</p>"""
    trust_password: "aws_sdk_directory_service.types.trust_password.TrustPassword"
    """<p>The trust password. The trust password must be the same password that was used when creating the trust relationship on the external domain.</p>"""
    trust_direction: "aws_sdk_directory_service.types.trust_direction.TrustDirection"
    """<p>The direction of the trust relationship.</p>"""
    trust_type: NotRequired["aws_sdk_directory_service.types.trust_type.TrustType"]
    """<p>The trust relationship type. <code>Forest</code> is the default.</p>"""
    conditional_forwarder_ip_addrs: NotRequired[
        "aws_sdk_directory_service.types.dns_ip_addrs.DnsIpAddrs"
    ]
    """<p>The IP addresses of the remote DNS server associated with RemoteDomainName.</p>"""
    conditional_forwarder_ipv6_addrs: NotRequired[
        "aws_sdk_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>The IPv6 addresses of the remote DNS server associated with RemoteDomainName.</p>"""
    selective_auth: NotRequired[
        "aws_sdk_directory_service.types.selective_auth.SelectiveAuth"
    ]
    """<p>Optional parameter to enable selective authentication for the trust.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrustRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["RemoteDomainName"] = value["remote_domain_name"]
    out["TrustPassword"] = value["trust_password"]
    import aws_sdk_directory_service.types.trust_direction

    out["TrustDirection"] = (
        aws_sdk_directory_service.types.trust_direction.serialize_aws_json_1_1(
            value["trust_direction"]
        )
    )
    if "trust_type" in value:
        import aws_sdk_directory_service.types.trust_type

        out["TrustType"] = (
            aws_sdk_directory_service.types.trust_type.serialize_aws_json_1_1(
                value["trust_type"]
            )
        )
    if "conditional_forwarder_ip_addrs" in value:
        import aws_sdk_directory_service.types.dns_ip_addrs

        out["ConditionalForwarderIpAddrs"] = (
            aws_sdk_directory_service.types.dns_ip_addrs.serialize_aws_json_1_1(
                value["conditional_forwarder_ip_addrs"]
            )
        )
    if "conditional_forwarder_ipv6_addrs" in value:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["ConditionalForwarderIpv6Addrs"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["conditional_forwarder_ipv6_addrs"]
            )
        )
    if "selective_auth" in value:
        import aws_sdk_directory_service.types.selective_auth

        out["SelectiveAuth"] = (
            aws_sdk_directory_service.types.selective_auth.serialize_aws_json_1_1(
                value["selective_auth"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrustRequest:
    out: CreateTrustRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("CreateTrustRequest.directory_id required")
    if "RemoteDomainName" in data:
        out["remote_domain_name"] = data["RemoteDomainName"]
    else:
        raise DeserializationError("CreateTrustRequest.remote_domain_name required")
    if "TrustPassword" in data:
        out["trust_password"] = data["TrustPassword"]
    else:
        raise DeserializationError("CreateTrustRequest.trust_password required")
    if "TrustDirection" in data:
        import aws_sdk_directory_service.types.trust_direction

        out["trust_direction"] = (
            aws_sdk_directory_service.types.trust_direction.deserialize_aws_json_1_1(
                data["TrustDirection"]
            )
        )
    else:
        raise DeserializationError("CreateTrustRequest.trust_direction required")
    if "TrustType" in data:
        import aws_sdk_directory_service.types.trust_type

        out["trust_type"] = (
            aws_sdk_directory_service.types.trust_type.deserialize_aws_json_1_1(
                data["TrustType"]
            )
        )
    if "ConditionalForwarderIpAddrs" in data:
        import aws_sdk_directory_service.types.dns_ip_addrs

        out["conditional_forwarder_ip_addrs"] = (
            aws_sdk_directory_service.types.dns_ip_addrs.deserialize_aws_json_1_1(
                data["ConditionalForwarderIpAddrs"]
            )
        )
    if "ConditionalForwarderIpv6Addrs" in data:
        import aws_sdk_directory_service.types.dns_ipv6_addrs

        out["conditional_forwarder_ipv6_addrs"] = (
            aws_sdk_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["ConditionalForwarderIpv6Addrs"]
            )
        )
    if "SelectiveAuth" in data:
        import aws_sdk_directory_service.types.selective_auth

        out["selective_auth"] = (
            aws_sdk_directory_service.types.selective_auth.deserialize_aws_json_1_1(
                data["SelectiveAuth"]
            )
        )
    return out
