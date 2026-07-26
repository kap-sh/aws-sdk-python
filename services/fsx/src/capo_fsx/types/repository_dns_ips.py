"""Generated from Smithy shape ``com.amazonaws.fsx#RepositoryDnsIps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.ip_address

RepositoryDnsIps: TypeAlias = list["capo_fsx.types.ip_address.IpAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryDnsIps) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RepositoryDnsIps:
    return list(data)
