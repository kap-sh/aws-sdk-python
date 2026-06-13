"""Generated from Smithy shape ``com.amazonaws.pcs#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

NetworkType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
    )
)


def serialize_aws_json_1_0(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkType value: {data!r}")
    return cast(NetworkType, data)
