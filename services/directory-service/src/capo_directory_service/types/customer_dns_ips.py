"""Generated from Smithy shape ``com.amazonaws.directoryservice#CustomerDnsIps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.ip_addr

CustomerDnsIps: TypeAlias = list["capo_directory_service.types.ip_addr.IpAddr"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerDnsIps) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomerDnsIps:
    return list(data)
