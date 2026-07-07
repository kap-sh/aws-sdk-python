"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheNFSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.nfs_version
    import aws_sdk_fsx.types.repository_dns_ips


class FileCacheNFSConfiguration(TypedDict, closed=True):
    version: NotRequired["aws_sdk_fsx.types.nfs_version.NfsVersion"]
    """<p>The version of the NFS (Network File System) protocol of the NFS data repository. The only supported value is <code>NFS3</code>, which indicates that the data repository must support the NFSv3 protocol.</p>"""
    dns_ips: NotRequired["aws_sdk_fsx.types.repository_dns_ips.RepositoryDnsIps"]
    """<p>A list of up to 2 IP addresses of DNS servers used to resolve the NFS file system domain name. The provided IP addresses can either be the IP addresses of a DNS forwarder or resolver that the customer manages and runs inside the customer VPC, or the IP addresses of the on-premises DNS servers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheNFSConfiguration) -> dict:
    out: dict = {}
    if "version" in value:
        import aws_sdk_fsx.types.nfs_version

        out["Version"] = aws_sdk_fsx.types.nfs_version.serialize_aws_json_1_1(
            value["version"]
        )
    if "dns_ips" in value:
        import aws_sdk_fsx.types.repository_dns_ips

        out["DnsIps"] = aws_sdk_fsx.types.repository_dns_ips.serialize_aws_json_1_1(
            value["dns_ips"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCacheNFSConfiguration:
    out: FileCacheNFSConfiguration = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        import aws_sdk_fsx.types.nfs_version

        out["version"] = aws_sdk_fsx.types.nfs_version.deserialize_aws_json_1_1(
            data["Version"]
        )
    if "DnsIps" in data:
        import aws_sdk_fsx.types.repository_dns_ips

        out["dns_ips"] = aws_sdk_fsx.types.repository_dns_ips.deserialize_aws_json_1_1(
            data["DnsIps"]
        )
    return out
