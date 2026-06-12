"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpAddrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.ip_addr

IpAddrs: TypeAlias = list["aws_sdk_directory_service.types.ip_addr.IpAddr"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddrs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpAddrs:
    return list(data)
