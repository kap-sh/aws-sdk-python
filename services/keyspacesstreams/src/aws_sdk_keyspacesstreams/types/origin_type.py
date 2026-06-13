"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#OriginType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_keyspacesstreams.errors import DeserializationError

OriginType: TypeAlias = Literal[
    "USER",
    "REPLICATION",
    "TTL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "REPLICATION",
        "TTL",
    )
)


def serialize_aws_json_1_0(value: OriginType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OriginType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginType value: {data!r}")
    return cast(OriginType, data)
