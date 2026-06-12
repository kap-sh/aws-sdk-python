"""Generated from Smithy shape ``com.amazonaws.fsx#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

NetworkType: TypeAlias = Literal[
    "IPV4",
    "DUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUAL",
    )
)


def serialize_aws_json_1_1(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkType value: {data!r}")
    return cast(NetworkType, data)
