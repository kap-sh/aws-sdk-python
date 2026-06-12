"""Generated from Smithy shape ``com.amazonaws.directoryservice#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

NetworkType: TypeAlias = Literal[
    "Dual-stack",
    "IPv4",
    "IPv6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Dual-stack",
        "IPv4",
        "IPv6",
    )
)


def serialize_aws_json_1_1(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkType value: {data!r}")
    return cast(NetworkType, data)
