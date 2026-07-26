"""Generated from Smithy shape ``com.amazonaws.directoryservice#NetworkType``."""

from typing import Literal, TypeAlias, cast

NetworkType: TypeAlias = Literal[
    "Dual-stack",
    "IPv4",
    "IPv6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkType:
    return cast(NetworkType, data)
