"""Generated from Smithy shape ``com.amazonaws.dax#ClusterEndpointEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dax.errors import DeserializationError

ClusterEndpointEncryptionType: TypeAlias = Literal[
    "NONE",
    "TLS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "TLS",
    )
)


def serialize_aws_json_1_1(value: ClusterEndpointEncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterEndpointEncryptionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClusterEndpointEncryptionType value: {data!r}"
        )
    return cast(ClusterEndpointEncryptionType, data)
