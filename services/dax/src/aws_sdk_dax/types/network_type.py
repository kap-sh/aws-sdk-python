"""Generated from Smithy shape ``com.amazonaws.dax#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dax.errors import DeserializationError

NetworkType: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dual_stack",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
        "dual_stack",
    )
)


def serialize_aws_json_1_1(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkType value: {data!r}")
    return cast(NetworkType, data)
