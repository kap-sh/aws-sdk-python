"""Generated from Smithy shape ``com.amazonaws.inspector#PrivateIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.private_ip

PrivateIpAddresses: TypeAlias = list["aws_sdk_inspector.types.private_ip.PrivateIp"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateIpAddresses) -> list:
    import aws_sdk_inspector.types.private_ip

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector.types.private_ip.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PrivateIpAddresses:
    import aws_sdk_inspector.types.private_ip

    out: PrivateIpAddresses = []
    for item in data:
        out.append(aws_sdk_inspector.types.private_ip.deserialize_aws_json_1_1(item))
    return out
