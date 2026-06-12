"""Generated from Smithy shape ``com.amazonaws.fsx#FlexCacheEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

FlexCacheEndpointType: TypeAlias = Literal[
    "NONE",
    "ORIGIN",
    "CACHE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ORIGIN",
        "CACHE",
    )
)


def serialize_aws_json_1_1(value: FlexCacheEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlexCacheEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlexCacheEndpointType value: {data!r}")
    return cast(FlexCacheEndpointType, data)
