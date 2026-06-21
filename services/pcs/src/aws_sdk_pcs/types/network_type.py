"""Generated from Smithy shape ``com.amazonaws.pcs#NetworkType``."""

from typing import Literal, TypeAlias, cast

NetworkType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetworkType:
    return cast(NetworkType, data)
