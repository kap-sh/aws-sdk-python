"""Generated from Smithy shape ``com.amazonaws.storagegateway#HostEnvironment``."""

from typing import Literal, TypeAlias, cast

HostEnvironment: TypeAlias = Literal[
    "VMWARE",
    "HYPER-V",
    "EC2",
    "KVM",
    "OTHER",
    "SNOWBALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostEnvironment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HostEnvironment:
    return cast(HostEnvironment, data)
