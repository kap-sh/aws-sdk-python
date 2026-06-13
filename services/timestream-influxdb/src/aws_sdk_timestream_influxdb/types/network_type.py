"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

NetworkType: TypeAlias = Literal[
    "IPV4",
    "DUAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUAL",
    )
)


def serialize_aws_json_1_0(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkType value: {data!r}")
    return cast(NetworkType, data)
