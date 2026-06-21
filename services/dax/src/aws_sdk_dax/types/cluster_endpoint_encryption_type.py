"""Generated from Smithy shape ``com.amazonaws.dax#ClusterEndpointEncryptionType``."""

from typing import Literal, TypeAlias, cast

ClusterEndpointEncryptionType: TypeAlias = Literal[
    "NONE",
    "TLS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEndpointEncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterEndpointEncryptionType:
    return cast(ClusterEndpointEncryptionType, data)
