"""Generated from Smithy shape ``com.amazonaws.directoryservice#CidrIpv6s``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.cidr_ipv6

CidrIpv6s: TypeAlias = list["aws_sdk_directory_service.types.cidr_ipv6.CidrIpv6"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CidrIpv6s) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CidrIpv6s:
    return list(data)
