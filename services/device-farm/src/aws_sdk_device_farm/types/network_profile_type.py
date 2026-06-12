"""Generated from Smithy shape ``com.amazonaws.devicefarm#NetworkProfileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

NetworkProfileType: TypeAlias = Literal[
    "CURATED",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURATED",
        "PRIVATE",
    )
)


def serialize_aws_json_1_1(value: NetworkProfileType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkProfileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkProfileType value: {data!r}")
    return cast(NetworkProfileType, data)
