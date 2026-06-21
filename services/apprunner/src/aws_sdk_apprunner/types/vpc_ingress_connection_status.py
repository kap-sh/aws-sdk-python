"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcIngressConnectionStatus``."""

from typing import Literal, TypeAlias, cast

VpcIngressConnectionStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING_CREATION",
    "PENDING_UPDATE",
    "PENDING_DELETION",
    "FAILED_CREATION",
    "FAILED_UPDATE",
    "FAILED_DELETION",
    "DELETED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcIngressConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VpcIngressConnectionStatus:
    return cast(VpcIngressConnectionStatus, data)
