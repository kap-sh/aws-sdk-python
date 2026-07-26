"""Generated from Smithy shape ``com.amazonaws.datasync#DnsIpList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.server_ip_address

DnsIpList: TypeAlias = list["capo_datasync.types.server_ip_address.ServerIpAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIpList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIpList:
    return list(data)
