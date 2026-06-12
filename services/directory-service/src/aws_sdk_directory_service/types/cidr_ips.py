"""Generated from Smithy shape ``com.amazonaws.directoryservice#CidrIps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.cidr_ip

CidrIps: TypeAlias = list["aws_sdk_directory_service.types.cidr_ip.CidrIp"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CidrIps) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CidrIps:
    return list(data)
